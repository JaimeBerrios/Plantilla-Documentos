# Observaciones Técnicas y Aspectos Pendientes de Revisión — SIGA-LoRa

**Documento:** Nota Técnica Interna de Control y Seguimiento (Fase 1)  
**Proyecto:** SIGA-LoRa: Sistema Inteligente de Gestión de Alertas  
**Subtítulo:** Prototipo de monitoreo inalámbrico de niveles de agua ante riesgos de inundación  
**Equipo de Trabajo:**
- Alexis Sebastián Castro Ramírez (Líder / Carné: CR0367042024)
- Jefferson Jared Bonilla Meléndez (Integrante / Carné: BM0749042022)
- Jaime Fernando Berrios Ortiz (Integrante / Carné: BO0310042024)
- *Cuarto Integrante:* Pendiente de confirmación  

---

Esta nota técnica recopila los puntos clave que el equipo debe gestionar, verificar o consensuar con el docente antes de la entrega final y el inicio de la Fase 2 (ensamble físico e informe final IEEE).

---

### 1. Cuarto Integrante del Equipo
- **Situación actual:** La guía técnica oficial de la Universidad Dr. Andrés Bello exige conformar grupos de **estrictamente 4 estudiantes**. Actualmente se dispone de los datos formales de 3 integrantes.
- **Acción requerida:** En la ficha oficial (PDF y Word) se dejó habilitada la fila con la indicación «Por confirmar». Se debe incorporar al cuarto compañero de clase y registrar su nombre completo y número de carné antes del cierre de firmas de conformidad.

---

### 2. Discrepancia en el Nombre de la Asignatura
- **Situación actual:** En la guía técnica de referencia proporcionada figuraba originalmente la asignatura *«Diseño de Sistemas de Seguridad de Redes»*, mientras que la instrucción actual define como asignatura oficial **«Sistemas Digitales»**, impartida por el **MduEV. Ing. Franklin Geovany Buruca Hernández**.
- **Acción requerida:** La ficha de propuesta corregida (`SIGA-LoRa_Fase1_Corregida.pdf`) ya utiliza «Sistemas Digitales» en el encabezado formal. Conviene reconfirmar administrativamente con el catedrático que la plantilla aplica a esta sección de la carrera sin requerir ajustes de nomenclatura.

---

### 3. Delimitación Territorial del Punto de Monitoreo
- **Situación actual:** Se ha definido la cuenca del Río Grande de San Miguel y la colonia Palo Blanco (San Miguel Centro) como áreas de referencia geográfica. Sin embargo, no se ha fijado la coordenada exacta o el cauce/colector pluvial puntual donde se ubicaría el nodo sensor (Estación A).
- **Acción requerida:** Seleccionar un punto específico para el estudio de caso (por ejemplo, el puente o badén sobre la calle Los Laureles o un colector pluvial crítico documentado en la colonia Palo Blanco). Esto permitirá calcular distancias reales de transmisión inalámbrica y estimar la altura de montaje del sensor ultrasónico JSN-SR04T.

---

### 4. Cuantificación y Verificación de Beneficiarios Directos
- **Situación actual:** 
  - La cifra de **74,650 hogares** proviene del *VII Censo de Población y VI de Vivienda 2024* de la ONEC/BCR y corresponde a la **totalidad del distrito de San Miguel** (municipio de San Miguel Centro), no a la colonia Palo Blanco de forma aislada.
  - Los reportes de **11 viviendas anegadas** (abril 2020) y **más de 15 viviendas afectadas** (septiembre 2020) en calle y senda Los Laureles corresponden a eventos periodísticos puntuales no acumulativos.
- **Acción requerida:** Realizar una delimitación comunitaria preliminar del área de influencia efectiva del nodo receptor comunitario (Estación B). La cantidad de beneficiarios directos debe mantenerse formalmente como *«pendiente de delimitación mediante levantamiento territorial»* para no incurrir en afirmaciones no sustentadas en la defensa académica.

---

### 5. Diagrama de Bloques Preliminar Definitivo
- **Situación actual:** Conforme a las instrucciones, se reservó el recuadro formal en la página 2 con la leyenda: *«Diagrama de bloques preliminar del sistema — pendiente de incorporación»*, eliminando el diagrama de ejemplo de la guía (EcoSensing-MUX) que no pertenecía al proyecto.
- **Acción requerida:** Desarrollar en la siguiente iteración el diagrama de bloques técnico definitivo que represente con exactitud la arquitectura de SIGA-LoRa:
  $$\text{Sensores (JSN-SR04T + Flotadores)} \longrightarrow \text{Compuertas 74HC} \longrightarrow \text{Arduino Uno} \longrightarrow \text{ESP32 + LoRa Tx} \stackrel{\text{RF 915 MHz}}{\dashrightarrow} \text{ESP32 + LoRa Rx} \longrightarrow \text{DEMUX 74HC238} \longrightarrow \text{LEDs + Buzzer}$$

---

### 6. Cotizaciones y Disponibilidad de Componentes en Plaza Local
- **Situación actual:** 
  - Los módulos principales (Arduino Uno, 2 ESP32, 2 RFM95W y 2 antenas LoRa 6 dBi) ya están disponibles en poder del equipo ($39.90 USD).
  - Los circuitos integrados lógicos (74HC08, 74HC32, 74HC04 y 74HC238) se cotizaron con referencias internacionales de LCSC / Texas Instruments ($4.60 USD considerando lotes mínimos).
  - Componentes pasivos, zócalos, convertidores de nivel y sensor ultrasónico ($43.74 USD) se basan en catálogos de Steren El Salvador y estimaciones de mercado.
- **Acción requerida:** 
  - Visitar sucursales locales (Steren San Miguel, Electrónica 2001 o proveedores en San Salvador) para verificar existencia física inmediata de los integrados CMOS serie **74HC**.
  - Evitar comprar sustitutos de la serie **74LS** salvo que se rediseñe la etapa de alimentación a 5V estrictos.
  - Cotizar localmente el sensor JSN-SR04T impermeable y los interruptores de nivel tipo flotador vertical.

---

### 7. Compatibilidad Eléctrica y Verificación de Radiofrecuencia (LoRa)
- **Frecuencia operativa:** Verificar que los transceptores HopeRF RFM95W adquiridos estén grabados y configurados por firmware para la banda ISM de **915 MHz** (aprobada por SIGET para Centroamérica/El Salvador), y no para 868 MHz (Europa) ni 433 MHz (Asia).
- **Adaptación de antena:** Comprobar que el conector de la antena externa omnidireccional (SMA hembra) encaje con el cable adaptador pigtail (U.FL/IPEX) que se soldará al pad de antena del RFM95W.
- **Niveles lógicos (3.3V vs 5V):** El Arduino Uno opera con señales I/O de 5V, mientras que el ESP32 y el transceptor LoRa RFM95W trabajan estrictamente a **3.3V**. Se debe emplear un módulo convertidor de nivel lógico bidireccional de 4 canales en las líneas de comunicación entre Arduino y ESP32 para evitar la destrucción irreversible de los pines de 3.3V.

