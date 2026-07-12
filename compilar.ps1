param(
    [string]$Archivo = "presentacion.tex"
)

try {
    $ErrorActionPreference = "Stop"
    $raiz = $PSScriptRoot
    $rutaSolicitada = if ([System.IO.Path]::IsPathRooted($Archivo)) {
        $Archivo
    } else {
        Join-Path $raiz $Archivo
    }

    $origen = (Resolve-Path $rutaSolicitada).Path
    $nombre = [System.IO.Path]::GetFileNameWithoutExtension($origen)
    $temporales = Join-Path $raiz ".build"
    $destino = Join-Path $raiz "pdf"
    $pdfTemporal = Join-Path $temporales "$nombre.pdf"
    $pdfFinal = Join-Path $destino "$nombre.pdf"
    $contenido = Get-Content -LiteralPath $origen -Raw
    $motor = if ($contenido -match '(?im)^%\s*!TEX\s+TS-program\s*=\s*lualatex\s*$') {
        "lualatex"
    } elseif ($contenido -match '(?im)^%\s*!TEX\s+TS-program\s*=\s*xelatex\s*$') {
        "xelatex"
    } elseif ($contenido -match '\\(?:RequirePackage|usepackage)\{fontspec\}') {
        "xelatex"
    } else {
        "pdflatex"
    }

    if (-not (Get-Command $motor -ErrorAction SilentlyContinue)) {
        throw "No se encontro '$motor'. Instala TeX Live o MiKTeX y verifica que el motor LaTeX este disponible en el PATH."
    }

    New-Item -ItemType Directory -Path $temporales -Force | Out-Null
    New-Item -ItemType Directory -Path $destino -Force | Out-Null

    # Permite que la presentacion encuentre archivos de plantilla/.
    $env:TEXINPUTS = "$raiz\plantilla;$raiz;"

    Push-Location $raiz
    try {
        1..2 | ForEach-Object {
            & $motor -interaction=nonstopmode -halt-on-error `
                -file-line-error -output-directory="$temporales" "$origen"
            if ($LASTEXITCODE -ne 0) {
                throw "La ejecucion $_ de $motor fallo con codigo $LASTEXITCODE."
            }
        }
    }
    finally {
        Pop-Location
    }

    if (-not (Test-Path -LiteralPath $pdfTemporal)) {
        throw "La compilacion termino sin generar $pdfTemporal."
    }

    Copy-Item -LiteralPath $pdfTemporal -Destination $pdfFinal -Force
    Write-Host "PDF creado con ${motor}: pdf/$nombre.pdf"
    exit 0
}
catch {
    Write-Error $_
    exit 1
}
