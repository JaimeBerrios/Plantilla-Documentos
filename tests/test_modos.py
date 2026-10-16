import contextlib
import io
from pathlib import Path
import shutil
import tempfile
import unittest
from unittest.mock import patch
from types import SimpleNamespace

import compilar


class ModosCompilacion(unittest.TestCase):
    def ejecutar(self, args, presentacion=False, fallo=False):
        original = compilar.ROOT
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            for name in ('datos.md', 'referencias.json', 'reporte.tex'):
                shutil.copy2(original / name, root / name)
            (root / 'pdf').mkdir()
            (root / 'reveal.js').mkdir()
            (root / 'pdf/reporte.pdf').write_bytes(b'%PDF-reporte anterior')
            (root / 'pdf/presentacion.pdf').write_bytes(b'%PDF-presentacion anterior')
            (root / 'reveal.js/index.html').write_text('HTML incompleto', encoding='utf-8')
            if presentacion:
                shutil.copy2(original / 'presentacion.tex', root / 'presentacion.tex')
                shutil.copy2(original / 'reveal.js/index.html', root / 'reveal.js/index.html')
            before = {name: (root / name).read_bytes() for name in ('pdf/presentacion.pdf', 'pdf/reporte.pdf', 'reveal.js/index.html')}
            for name in ('isotipo-azul.png', 'logo-facultad.png', 'acreditacion.png'):
                p = root / 'assets/img/institucional' / name
                p.parent.mkdir(parents=True, exist_ok=True)
                p.touch()
            (root / 'assets/fonts').mkdir()
            (root / 'assets/fonts/firma.otf').touch()
            compiled = []

            def fake_compile(command, **kwargs):
                name = Path(command[-1]).stem
                compiled.append(name)
                if fallo:
                    return SimpleNamespace(returncode=1)
                staging = Path(command[command.index('--outdir') + 1])
                (staging / f'{name}.pdf').write_bytes(b'%PDF-nuevo')
                return SimpleNamespace(returncode=0)

            with patch.object(compilar, 'ROOT', root), patch.object(compilar, 'get_compiler', return_value='tectonic'), patch.object(compilar.subprocess, 'run', side_effect=fake_compile), patch('sys.argv', ['compilar.py'] + args), contextlib.redirect_stdout(io.StringIO()):
                if fallo:
                    with self.assertRaises(RuntimeError):
                        compilar.main()
                else:
                    compilar.main()
            after = {name: (root / name).read_bytes() for name in before}
            if not presentacion:
                self.assertFalse((root / '.build/referencias-presentacion.tex').exists())
            return compiled, before, after

    def test_por_defecto_no_requiere_fuentes_presentacion_y_conserva_salidas(self):
        compiled, before, after = self.ejecutar([])
        self.assertEqual(compiled, ['reporte'])
        self.assertNotEqual(before['pdf/reporte.pdf'], after['pdf/reporte.pdf'])
        for name in ('pdf/presentacion.pdf', 'reveal.js/index.html'):
            self.assertEqual(before[name], after[name])

    def test_verificar_reporte_no_compila_ni_modifica(self):
        compiled, before, after = self.ejecutar(['--verificar'])
        self.assertEqual(compiled, [])
        self.assertEqual(before, after)

    def test_presentacion_requiere_opcion_explicita(self):
        compiled, before, after = self.ejecutar(['--con-presentacion'], presentacion=True)
        self.assertEqual(compiled, ['presentacion', 'reporte'])
        self.assertNotEqual(before['pdf/presentacion.pdf'], after['pdf/presentacion.pdf'])
        self.assertIn(b'referencias:inicio', after['reveal.js/index.html'])

    def test_fallo_conserva_los_entregables(self):
        _, before, after = self.ejecutar([], fallo=True)
        self.assertEqual(before, after)
