# Datos del trabajo

Edita los valores después de `:` y las filas de integrantes. Conserva los nombres
de los campos y los encabezados: al compilar se trasladan a `pdf/propuesta.pdf`.
Escribe texto normal, sin comandos LaTeX. No uses `|` dentro de una celda.

## Datos generales

- Título: SIGA-LoRa: Sistema Inteligente de Monitoreo y Alerta de Crecidas e Inundaciones mediante Arduino, ESP32, Comunicación LoRa y Lógica Digital.
- Subtítulo: Prototipo universitario funcional de electrónica digital aplicada al monitoreo ambiental y comunicación inalámbrica
- Título corto: SIGA-LoRa
- Institución: Universidad Dr. Andrés Bello
- Facultad: Facultad de Tecnología e Innovación
- Asignatura: Diseño de Sistemas de Seguridad de Redes
- Docente: Nombre del docente
- Grupo: Grupo 01
- Lugar y fecha: San Miguel, sábado 10 de octubre de 2026
- Firma: Jaime Berrios

## Integrantes

| Nombre | Código |
|---|---|
| Estudiante líder: nombre pendiente | Carné pendiente |
| Estudiante 2: nombre pendiente | Carné pendiente |
| Estudiante 3: nombre pendiente | Carné pendiente |
| Estudiante 4: nombre pendiente | Carné pendiente |

## Fase 1: Ficha de Propuesta de Proyecto

- Límite de extensión: máximo 2 páginas.
- Eje temático: Medio ambiente (gestión de residuos, ahorro energético, calidad de aire/agua, etc.).
- Requisitos técnicos: lógica combinacional pura (Karnaugh), módulo MUX/DEMUX, microcontrolador Arduino, maquetado y soldadura física.
- Diagrama de bloques: Sensores → Arduino Uno / lógica combinacional física → ESP32 → LoRa → enlace inalámbrico → LoRa → ESP32 → DEMUX → indicadores y alarma.
- Presupuesto estimado: lista de componentes, aplicación y costos unitario/total.
- Validación docente: firmas de entrega y aprobación requeridas antes de compras o ensamble.

## Problemática y justificación

El proyecto se inspira en el riesgo de inundaciones en San Miguel, El Salvador, con interés en la cuenca del Río Grande de San Miguel y la colonia Palo Blanco, San Miguel Centro. Se estudiarán lluvias intensas, aumentos del nivel del agua, desbordamientos y deficiencias de drenaje. La relación hidrológica directa entre el río y las inundaciones de Palo Blanco está pendiente de demostración; no debe afirmarse sin evidencia.

La propuesta investigará el monitoreo automatizado del nivel del agua, la validación mediante lógica digital física y la comunicación inalámbrica de advertencias entre dos estaciones LoRa. Los beneficios son potenciales, no resultados demostrados. Cantidad de beneficiarios directos pendiente de delimitación y verificación.

## Indicaciones del docente

Seguir la guía local `info/GUIA TECNICA DE PROPUESTAS DE PROYECTOS.pdf`, especialmente la Fase 1, con entrega el sábado 10 de octubre de 2026. El equipo será de cuatro estudiantes. Solicitar la aprobación del catedrático antes de comprar o ensamblar los componentes faltantes. Los detalles del encargo aportados por el usuario se conservan a continuación como instrucciones para un desarrollo posterior.

## Contenido y fuentes

La información siguiente fue proporcionada por el usuario. Las fuentes, precios, especificaciones y antecedentes todavía requieren verificación; registrarlos aquí no equivale a haberlos investigado o validado. El compilador sincroniza únicamente los datos generales y los integrantes.

## Encargo maestro — alcance pendiente de ejecución

Actuar como un equipo multidisciplinario compuesto por un ingeniero electrónico, especialista en sistemas embebidos, investigador ambiental, especialista en gestión de riesgos de inundaciones y redactor de documentos técnicos universitarios.

Desarrollar una Ficha de Propuesta de Proyecto siguiendo estrictamente la guía técnica de la Universidad Dr. Andrés Bello, Facultad de Tecnología e Innovación, asignatura Diseño de Sistemas de Seguridad de Redes. Máximo dos páginas, redacción académica formal, información verificable, fuentes confiables y presupuesto técnicamente justificado.

Por ahora, este encargo queda registrado únicamente en datos.md. No implica ejecutar la investigación, redactar la ficha final ni compilar en esta actualización. Los nombres y carnés están pendientes; docente, grupo y firma conservados arriba no deben interpretarse como datos confirmados del equipo.

### 1. Identificación y delimitación del proyecto

- Nombre preliminar: SIGA-LoRa: Sistema Inteligente de Monitoreo y Alerta de Crecidas e Inundaciones mediante Arduino, ESP32, Comunicación LoRa y Lógica Digital.
- Institución: Universidad Dr. Andrés Bello.
- Facultad: Tecnología e Innovación.
- Asignatura: Diseño de Sistemas de Seguridad de Redes.
- Equipo: cuatro estudiantes; líder y tres integrantes, todos con nombre y carné pendientes.
- Entrega Fase 1: sábado 10 de octubre de 2026.
- Naturaleza: prototipo universitario funcional de electrónica digital aplicada al monitoreo ambiental y comunicación inalámbrica.
- Caso de estudio: San Miguel, El Salvador.
- Área hidrológica de interés: cuenca del Río Grande de San Miguel.
- Comunidad potencialmente beneficiaria: colonia Palo Blanco, San Miguel Centro.

No afirmar que el Río Grande provoca directamente las inundaciones de Palo Blanco sin evidencia hidrológica o cartográfica. Existen antecedentes de desbordamientos del río y antecedentes separados de inundaciones urbanas de la colonia por drenajes saturados y escorrentía. Si no se demuestra una relación directa, formular el proyecto como un prototipo de monitoreo del nivel del agua y advertencia ante inundaciones, aplicable a ríos, canales y puntos de drenaje urbano. No presentarlo como sistema oficial de protección civil ni tecnología certificada de alerta temprana.

### 2. Problemática ambiental y antecedentes por verificar

Investigar y redactar un diagnóstico de aproximadamente 150 a 200 palabras sobre el riesgo de inundaciones por lluvias intensas, aumentos del nivel de los ríos, desbordamientos y deficiencias del drenaje de aguas lluvias. Explicar el problema concreto, causas y consecuencias documentadas, importancia de monitorear niveles, limitaciones de un sistema exclusivamente manual y justificación para investigar una alerta inalámbrica. Evitar exageraciones, predicciones y estadísticas sin respaldo.

Antecedentes aportados:

1. Dirección General de Protección Civil, 11 de noviembre de 2014: desbordamientos del Río Grande de San Miguel en Santa Fidelia, La Canoa y El Nancito; inundaciones en Palo Blanco por saturación de drenajes.
   https://www.proteccioncivil.gob.sv/2014/11/11/informe/
2. Ministerio de Medio Ambiente y Recursos Naturales, agosto de 2021: nivel de 8.52 metros en la estación La Canoa, equivalente al 89 % de la condición de banca llena de esa estación. Es un antecedente histórico, no un umbral universal de alerta.
   https://www.ambiente.gob.sv/se-mantienen-tormentas-de-moderadas-a-fuertes-por-paso-de-ondas-tropicales-en-los-proximos-dias/
3. Protección Civil, 22 de octubre de 2025: alerta verde por lluvias y riesgo de anegamientos en sectores de la cuenca del Río Grande de San Miguel.
   https://www.proteccioncivil.gob.sv/2025/10/22/alerta-verde-por-lluvias-asociadas-a-la-influencia-indirecta-de-la-tormenta-tropical-melissa-y-la-presencia-de-vaguadas-en-la-region-22-octubre-2025/
4. La Prensa Gráfica, 3 de abril de 2020: inundación de 11 viviendas en calle Los Laureles, colonia Palo Blanco, después de una tormenta y el desplome de un muro.
   https://www.laprensagrafica.com/elsalvador/Lluvia-inunda-11--viviendas-y-calle-20200402-0122.html
5. La Prensa Gráfica, 29 de septiembre de 2020: daños en más de 15 viviendas de la senda Los Laureles, colonia Palo Blanco, vinculados con filtraciones y desvío de aguas lluvias.
   https://www.laprensagrafica.com/elsalvador/Filtracion-de-agua-afecta-residencias-20200928-0052.html

No sumar las viviendas de eventos distintos ni presentarlas como censo de beneficiarios; podrían ser viviendas repetidas.

### 3. Justificación socioambiental

Redactar una justificación académica para desarrollar un sistema económico que detecte condiciones de nivel, procese señales digitales y comunique advertencias sin Wi-Fi en el enlace entre estaciones. Argumentar el valor del monitoreo automatizado de una variable ambiental, la comunicación entre dos puntos mediante LoRa, la validación con circuitos lógicos físicos, los indicadores visuales y sonoros y la posible ampliación en investigaciones futuras.

Distinguir beneficios potenciales de demostrados. No afirmar que salva vidas, garantiza evacuaciones, evita inundaciones o predice crecidas; no se han comprobado esos resultados.

### 4. Población objetivo y beneficiarios

- Población objetivo preliminar: habitantes de Palo Blanco, especialmente sectores con antecedentes de anegamientos durante lluvias intensas.
- Beneficiarios directos potenciales: residentes de viviendas dentro del área hipotética de cobertura de la estación comunitaria receptora.
- Beneficiarios indirectos potenciales: organizaciones comunitarias, comisiones de protección civil y personal de respuesta ante emergencias.

Investigar datos oficiales de población o viviendas de la colonia en el Censo de Población y Vivienda 2024 del Banco Central de Reserva: https://censo2024.bcr.gob.sv/

Si no existe un dato desagregado verificable, escribir literalmente: "Cantidad de beneficiarios directos pendiente de delimitación y verificación". No inventar población, hogares, distancias al río ni personas protegidas. Si otra comunidad resulta más directamente expuesta al río, proponerla como alternativa explicada, sin sustituir automáticamente Palo Blanco.

### 5. Objetivos del proyecto

Objetivo general propuesto:

"Diseñar un prototipo funcional de monitoreo del nivel del agua y comunicación inalámbrica de advertencias, mediante Arduino, ESP32, tecnología LoRa y circuitos lógicos combinacionales, para demostrar una alternativa tecnológica de vigilancia ambiental ante condiciones asociadas a inundaciones".

Formular cuatro objetivos específicos medibles que contemplen:

1. Detectar niveles de agua mediante sensores.
2. Implementar compuertas físicas, tablas de verdad y simplificación booleana.
3. Transmitir estados de monitoreo a la estación receptora mediante LoRa.
4. Construir y evaluar una maqueta funcional con conexiones soldadas sobre placas perforadas.

### 6. Hardware disponible

Componentes comprados anteriormente en AliExpress. Los importes son valores comparables de publicaciones o historiales, no precios reales pagados ni facturas del equipo.

| Cantidad | Componente | Valor unitario referencial USD |
|---|---|---:|
| 2 | ESP32 | 4.37 |
| 2 | Módulos LoRa RFM95/SX1276 | 7.25 |
| 2 | Antenas omnidireccionales 6 dBi | 15.63 |
| 1 | Arduino Uno | 5.10 |
| 1 | Arduino Nano | 2.70 |

Valor referencial total aportado: **$62.30**. El Nano puede permanecer como reserva y no instalarse en la primera versión.

Referencias comerciales por verificar, incluyendo correspondencia de variantes con el hardware disponible:

- ESP32: https://es.pricearchive.org/aliexpress.com/item/1005006613312645
- RFM95W: https://sv.pricearchive.org/aliexpress.com/item/1005008598595141
- Antena LoRa 6 dBi: https://www.pricearchive.org/aliexpress.com/item/1005007226356668
- Arduino Uno: https://es.pricearchive.org/aliexpress.com/item/1005007938089405
- Arduino Nano: https://www.pricearchive.org/aliexpress.com/item/1005003102378550

### 7. Componentes adicionales y presupuesto provisional

Todos los importes se expresan en dólares estadounidenses y requieren verificación.

#### A. Sensores y circuitos digitales

| Componente | Cantidad requerida | Presupuesto referencial USD |
|---|---|---:|
| Sensor ultrasónico impermeable JSN-SR04T | 1 | 2.12 |
| Interruptores de nivel tipo flotador | 3 | 3.87 |
| CI 74HC08 AND, DIP-14 | 1 | 0.52 |
| CI 74HC32 OR, DIP-14 | 1 | 0.57 |
| CI 74HC04 NOT, DIP-14 | 1, comprar lote de 5 | 0.90 |
| CI 74HC238 DEMUX, DIP-16 | 1, comprar lote de 5 | 1.12 |

Fuentes aportadas:

- JSN-SR04T, comparable AliExpress: https://es.pricearchive.org/aliexpress.com/item/1005003213157894
- Flotadores, variante económica; verificar precio de tres unidades: https://www.pricearchive.org/aliexpress.com/item/1005012090376652
- 74HC08, LCSC: https://lcsc.com/product-detail/Gates_Texas-Instruments_C2887.html
- 74HC32, LCSC: https://www.lcsc.com/product-detail/74-Series_TI_SN74HC32N_SN74HC32N_C2894.html
- 74HC04, LCSC: https://www.lcsc.com/es/product-detail/C669327.html
- 74HC238, LCSC: https://www.lcsc.com/product-detail/signal-switches-multiplexers-decoders_hgsemi-74hc238n_C5310756.html

Distinguir lotes mínimos de compra y cantidad instalada. Verificar disponibilidad, envío, impuestos y conveniencia de equivalentes locales.

#### B. Montaje físico, alertas y accesorios

| Componente | Cantidad | Precio total referencial USD |
|---|---|---:|
| Zócalos DIP-14 | 3 | 0.63 |
| Zócalo DIP-16 | 1 | 0.20 |
| Baquelas perforadas modelo 400, soldables | 2 | 6.98 |
| Baquelas perforadas modelo 405, soldables | 2 | 2.98 |
| LEDs indicadores | 4 | 0.80 |
| Mini buzzer BGD08 | 1 | 1.00 |
| Transistor BC337 | 1 | 0.21 |
| Resistencias surtidas de ½ W | 20 | 1.00 |
| Alambre estañado 22 AWG | 8 metros | 2.00 |
| Soldadura SOL60-020 de 17 g | 1 | 3.99 |

Fuentes oficiales de Steren El Salvador aportadas:

- Circuitos y zócalos: https://www.steren.com.sv/proyectos-de-electronica/circuitos-integrados
- Baquelas: https://www.steren.com.sv/proyectos-de-electronica/baquelas-y-accesorios-de-c-i
- LEDs: https://www.steren.com.sv/proyectos-de-electronica/optoelectronica
- Buzzer: https://www.steren.com.sv/proyectos-de-electronica/buzzers-zumbadores
- Transistores: https://www.steren.com.sv/proyectos-de-electronica/transistores
- Resistencias: https://www.steren.com.sv/linea-estudiantil/potenciometros-y-resistencias
- Alambre: https://www.steren.com.sv/alambre-esta-ado-para-conexiones-22-awg-color-negro.html
- Soldadura y herramientas: https://www.steren.com.sv/herramientas/cautines-y-accesorios

Subtotal aportado de materiales adicionales A + B con referencias identificadas: **$28.89**. Combina vendedores; no constituye cotización local conjunta ni confirmación de inventario.

#### C. Reservas de planificación pendientes de cotización

Estos importes no son precios publicados por un proveedor.

| Material | Reserva USD |
|---|---:|
| Adaptador de señales 5 V/3.3 V | 2.00 |
| Condensadores de desacoplo | 0.40 |
| Adaptadores de RF, conectores o placas adaptadoras LoRa | 6.00 |
| Cables USB necesarios | 6.00 |
| Alimentación USB para ambas estaciones | 10.00 |
| Conectores y borneras | 3.00 |
| Materiales de construcción de maqueta | 8.00 |
| Recipiente para simular el cauce | 4.00 |

Reserva total no cotizada: **$39.40**. Considerar transporte, envío internacional e impuestos cuando puedan determinarse. Se aporta una referencia de cautín CAU-105 de $5.00 en Steren: verificar y registrar como herramienta opcional si el equipo ya dispone de uno.

#### D. Resumen financiero provisional aportado

- Equipos disponibles, valor referencial: **$62.30**.
- Componentes adicionales con precio de referencia: **$28.89**.
- Reservas sin cotizar: **$39.40**.
- Proyección total de inventario, adquisiciones y reservas: **$130.59**.
- Proyección de desembolso adicional: **$68.29**.
- El Nano ($2.70) está incluido en inventario; puede excluirse del costo técnico instalado si queda de reserva.

Las cifras son preliminares, variables y no incluyen necesariamente envío internacional ni impuestos de importación. Investigar también https://electronica2001es.com/ y priorizar Electrónica 2001 y Steren cuando haya equivalentes disponibles con precios verificables. En caso contrario, conservar referencias internacionales o indicar "pendiente de cotización". No inventar productos ni precios.

### 8. Arquitectura de dos estaciones

#### Estación A — Monitoreo

Ubicación simulada: proximidades de un cauce o punto de acumulación de agua.

Hardware: Arduino Uno, JSN-SR04T, tres flotadores a distintas alturas, compuertas físicas AND/OR/NOT, ESP32, LoRa RFM95/SX1276 y antena compatible.

El ultrasónico mide la distancia a la superficie; los flotadores detectan agua en niveles definidos. Arduino lee y procesa sensores. Las compuertas deben implementar funciones concretas de validación y generación de estados. Arduino comunica mediciones o estados al ESP32 mediante una interfaz eléctricamente compatible; el ESP32 transmite por LoRa.

#### Estación B — Centro receptor comunitario

Hardware: ESP32, LoRa RFM95/SX1276, antena compatible, DEMUX físico 74HC238, LEDs, buzzer y circuito de potencia apropiado.

El ESP32 recibe mediciones o estados y entrega señales de selección al DEMUX, que activa la salida correspondiente:

| Código | Estado propuesto | Indicador |
|---|---|---|
| 00 | Normal | LED verde |
| 01 | Precaución | LED amarillo |
| 10 | Nivel alto | LED naranja |
| 11 | Condición crítica | LED rojo y buzzer |

Los umbrales son experimentales y deben calibrarse para la maqueta. Agregar señal de fallo o pérdida de comunicación independiente del estado normal. El DEMUX distribuye o selecciona señales eléctricas locales; no comunica directamente con instituciones. El envío a teléfonos o instituciones requeriría tecnología adicional.

### 9. Diseño lógico y fundamentación por desarrollar

Entradas: F1, flotador inferior; F2, intermedio; F3, superior. Un valor 1 indica activación.

| F1 | F2 | F3 | Interpretación físicamente coherente |
|---|---|---|---|
| 0 | 0 | 0 | Nivel normal |
| 1 | 0 | 0 | Precaución |
| 1 | 1 | 0 | Nivel alto |
| 1 | 1 | 1 | Nivel crítico |

Examinar las otras combinaciones como posibles fallas de sensor o cableado; no clasificarlas automáticamente como seguras. Proponer ecuaciones implementables con compuertas reales y simplificarlas con mapas de Karnaugh. Explicar la función concreta de 74HC08, 74HC32 y 74HC04, sin componentes de adorno académico.

Describir la selección del 74HC238 y su tabla de salidas. Se pueden emplear dos líneas de selección, fijar la tercera y controlar las habilitaciones. Verificar con la hoja de datos del integrado exacto.

- Referencia técnica del DEMUX: https://www.ti.com/lit/ds/symlink/cd74hc238.pdf
- Referencia SX1276: https://www.semtech.com/products/wireless-rf/lora-connect/sx1276

Consideraciones obligatorias para el diseño:

- ESP32 y RFM95 usan señales de 3.3 V; Uno y Nano convencionales usan lógica de 5 V. Diseñar la adaptación de niveles.
- Confirmar alimentación de cada integrado.
- Usar resistencias limitadoras para LEDs.
- No conectar buzzer o sirenas de potencia directamente al DEMUX cuando excedan su capacidad de salida.
- Incluir desacoplo y tierras apropiadas.
- Confirmar módulos LoRa exactos e interfaz de antena.
- Verificar banda, normativa de SIGET y límites permitidos antes de transmitir.
- No prometer alcance sin pruebas de campo.

### 10. Diagrama de bloques pendiente

Generar un diagrama académico claro y profesional, apropiado para insertar en la ficha:

- Monitoreo: sensores de nivel y ultrasónico → Arduino Uno / lógica combinacional física → ESP32 → módulo LoRa → antena.
- Enlace: comunicación inalámbrica LoRa entre estaciones.
- Receptor: antena → LoRa → ESP32 → DEMUX 74HC238 → indicadores visuales y alarma sonora.

Representar entradas de control, salidas y alimentación; distinguir procesamiento digital, comunicación y actuadores.

### 11. Maqueta física

- Sección A: río o quebrada representado por recipiente o canal transparente con agua de nivel variable manualmente; ultrasónico sobre la superficie y flotadores a distintas alturas.
- Sección B: comunidad representada con cuatro indicadores y alarma sonora.
- Separar físicamente las estaciones y comunicar mediante LoRa, sin cables de señal entre ellas.
- Montaje final obligatorio soldado sobre placas perforadas o PCB; no usar protoboards sin soldadura en el prototipo final.
- Simular previamente en Logisim, Tinkercad o A+, según disponibilidad y compatibilidad. Si LoRa no puede simularse, explicar su validación separada.
- No utilizar componentes eléctricos expuestos al agua.

### 12. Pruebas y resultados esperados

Proponer pruebas controladas de laboratorio para:

1. Lectura del nivel del agua.
2. Activación individual de flotadores.
3. Validación de tablas de verdad.
4. Operación real de compuertas físicas.
5. Selección de salidas del DEMUX.
6. Comunicación entre las dos estaciones LoRa.
7. Activación de indicadores y buzzer.
8. Desconexión del transmisor para detectar pérdida de comunicación.
9. Repetición de mediciones para evaluar estabilidad.

Distinguir resultados esperados de obtenidos. No inventar resultados experimentales, precisión, alcance ni tiempos de respuesta.

### 13. Formato obligatorio de la Fase 1

Incluir en este orden:

1. Nombre del proyecto e integrantes.
2. Problemática ambiental identificada y justificación.
3. Población objetivo y beneficiarios directos.
4. Diagrama preliminar de bloques.
5. Presupuesto estimado: cantidad, descripción, aplicación, precio unitario y total.
6. Firmas de conformidad y validación: firma del líder, fecha de entrega, dictamen del docente, observaciones, firma y sello del catedrático.

Máximo dos páginas para la ficha principal. Si bibliografía detallada o fuentes de precios no caben, preparar respaldo independiente identificado como material complementario cuya presentación dependerá de autorización docente. No omitir apartados obligatorios.

### 14. Referencias bibliográficas

Usar estilo IEEE con autor institucional o autor de noticia, título exacto, fecha de publicación cuando esté disponible, institución o medio, URL y fecha de consulta real.

Priorizar instituciones públicas salvadoreñas, publicaciones científicas, hojas de datos oficiales y catálogos verificables. No inventar títulos, autores, años, estadísticas, precios ni población. Separar fuentes ambientales, técnicas y de precios.

### 15. Entregables solicitados para la futura ejecución

1. Ficha de Propuesta de Proyecto terminada, académica, clara y de máximo dos páginas.
2. Presupuesto detallado de respaldo con componentes, cantidades, precios publicados, reservas, proveedores, enlaces y subtotales correctamente calculados.
3. Diagrama de bloques.
4. Tabla de verdad preliminar y ecuaciones booleanas que demuestren compuertas y DEMUX físicos.
5. Bibliografía confiable IEEE.
6. Lista breve de validaciones pendientes: población de Palo Blanco, relación hidrológica con el Río Grande, frecuencia real de módulos LoRa y precios finales de materiales no cotizados.

Respetar literalmente la guía. Marcar como pendiente lo no verificable, sin completar con suposiciones. El resultado deberá ser técnicamente defendible, realista en costos y adecuado para solicitar aprobación del catedrático antes de comprar o ensamblar componentes faltantes.

Instrucción de inicio del encargo futuro: "Comienza redactando la Fase 1 completa". No ejecutar esta instrucción mientras el alcance autorizado sea únicamente actualizar datos.md.
