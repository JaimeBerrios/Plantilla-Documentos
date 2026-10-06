1. Descripción del proyecto

1.1. Problema:  
La agencia de viajes "SAMI Travels & Tours" (legalmente GRUPO SAMI S.A.S DE C.V.), ubicada en San Miguel, El Salvador, se dedica a la comercialización de servicios turísticos, paquetes vacacionales y reservas de boletos. Actualmente, la empresa enfrenta dificultades operativas debido a que la gestión de cotizaciones complejas —que combinan vuelos, tours guiados y alojamiento— se realiza de manera manual. Esta falta de automatización y la ausencia de un sistema centralizado para el seguimiento de prospectos comerciales generan lentitud en los tiempos de respuesta, pérdida de información en el embudo de ventas y dificultades para que la Gerencia General mantenga un control visual sobre el estado de cada cliente. Es fundamental comprender este problema de negocio antes de proponer una solución tecnológica, ya que el desarrollo debe orientarse a resolver esta necesidad operativa real.

1.2. Justificación:  
Para resolver la problemática descrita, se propone el desarrollo de una Solución End-to-End basada en una Arquitectura de Aplicación Web Progresiva (PWA). La construcción de esta plataforma permitirá estandarizar las operaciones comerciales de la agencia, pasando de un manejo manual y fragmentado a un ecosistema digital centralizado. La integración de un motor de Inteligencia Artificial (API de Google Gemini) reducirá drásticamente el tiempo de creación de itinerarios y cotizaciones, mientras que un CRM interno permitirá gestionar el estado de las ventas. Esto justifica la inversión de tiempo y recursos, ya que el sistema no solo organizará la información, sino que proporcionará un embudo de ventas de alta conversión, mejorando la competitividad de la agencia en el sector turístico.

1.3. Objetivos:  
General:  
Desarrollar e implementar una plataforma web progresiva (PWA) integral para SAMI Travels & Tours que centralice la gestión de clientes, automatice la creación de cotizaciones turísticas y ofrezca un catálogo digital interactivo, mejorando la eficiencia operativa y los tiempos de respuesta.

Específicos:

* Construir el módulo SAMI Admin (CRM) equipado con un tablero Kanban visual para el seguimiento y administración del ciclo de vida de los clientes.  
  * Integrar un motor de IA generativa para agilizar la construcción dinámica de cotizaciones (vuelos y tours) y generar automáticamente documentos en formato PDF corporativo.  
  * Desarrollar un portal público indexable (B2C) y un portal privado de clientes que permita la autenticación segura y la aprobación digital de propuestas.

1.4. Alcance  
El proyecto abarca el ciclo completo de desarrollo del software, incluyendo el análisis, diseño, programación, pruebas e implementación en la nube.

Elementos incluidos en el alcance: El desarrollo abarcará tres módulos principales: un portal público B2C con soporte offline parcial (Service Worker), un portal privado para clientes (flujo de aprobación de cotizaciones) y un CRM administrativo (SAMI Admin). Técnicamente, incluirá el desarrollo del backend (Python/Django), frontend (Tailwind CSS, Vanilla JS), integración de bases de datos (MySQL), generación de PDFs (WeasyPrint) y el despliegue en un servidor VPS (DigitalOcean) utilizando contenedores Docker. Se incluirá también la configuración de analítica SEO básica (GA4, [Schema.org](http://Schema.org)).  
Límites y exclusiones: Para evitar el crecimiento descontrolado del proyecto (scope creep), no se incluirá dentro de esta fase la integración de pasarelas de pago directo con tarjetas de crédito (las cotizaciones se aprobarán digitalmente, pero el cobro se gestionará externamente), ni se desarrollarán aplicaciones móviles nativas para tiendas de aplicaciones (App Store/Play Store), ya que la arquitectura PWA cubrirá la necesidad de acceso móvil desde el navegador.

1.5. Usuarios  
Para asegurar que el diseño y las funcionalidades del sistema respondan adecuadamente a las necesidades operativas del negocio, se han definido los siguientes perfiles o roles de usuarios que interactuarán con la plataforma:

Usuarios Administrativos y Operativos: Comprende al personal interno de la agencia, específicamente la Gerencia General y los asesores o agentes de viajes. Este grupo tendrá acceso restringido al módulo SAMI Admin (CRM) y será responsable de alimentar el catálogo de destinos turísticos, generar las cotizaciones dinámicas, administrar el directorio y dar seguimiento continuo al embudo de ventas a través del tablero Kanban.

Clientes Finales (B2C / B2B): Representa a las personas naturales o clientes corporativos interesados en adquirir paquetes vacacionales, tours o boletos aéreos. Su interacción inicial se dará a través del portal público para la exploración indexable del catálogo de destinos; posteriormente, utilizarán un portal privado para clientes donde podrán autenticarse, consultar el detalle de sus itinerarios en formato PDF y realizar la aprobación digital de las propuestas comerciales.

**2\. Componentes que deberá integrar el proyecto.**

- Ingeniería de requisitos: **requisitos de negocio, usuario, funcionales y no funcionales.**

- **Requisitos de negocio:**

**Sami Travel & Tours** es un proyecto en el cual debe de permitir gestionar digitalmente el proceso de elaboración y seguimiento de cotizaciones turísticas. La cual le permitirá al usuario establecer fecha, tipo de cotización ya sea para un viaje privado con categorías, tours ida y vuelta y recomendaciones de viaje. Además cuenta con el apoyo de un agente de IA que facilita la documentación y elaboración de itinerarios turísticos. 

| ID | Requisito de negocio |
| ----- | ----- |
|  **RN-01** | SAMI Travels & Tours deberá disponer de una plataforma digital que centralice y apoye la gestión de sus servicios turísticos y procesos comerciales. |
|  **RN-02** | El sistema deberá apoyar la comercialización digital de paquetes vacacionales, boletos aéreos, tours guiados y otros servicios turísticos ofrecidos por SAMI. |
|  **RN-03** | La solución deberá permitir mejorar la presencia digital de SAMI mediante un portal público accesible e indexable. |
|  **RN-04** | El sistema deberá facilitar la captación de potenciales clientes mediante la consulta de destinos, paquetes y servicios turísticos. |
|  **RN-05** | El sistema deberá reducir la dependencia de procesos manuales para la elaboración y gestión de cotizaciones. |
|  **RN-06** | La plataforma deberá centralizar la información necesaria para gestionar clientes, destinos, servicios y cotizaciones. |
|  **RN-07** | El sistema deberá facilitar el seguimiento del ciclo comercial de una solicitud, desde el interés inicial del cliente hasta la elaboración y entrega de una cotización. |
|  **RN-08** | La solución deberá proporcionar herramientas que permitan al personal de SAMI gestionar eficientemente las oportunidades comerciales. |
|  **RN-09** | El sistema deberá permitir generar documentos de cotización profesionales y estandarizados. |
|  **RN-10** | La solución deberá incorporar herramientas de inteligencia artificial como apoyo para reducir el tiempo de elaboración de itinerarios. |
|  **RN-11** | El uso de inteligencia artificial deberá estar sujeto a revisión y aprobación por parte del personal autorizado de SAMI antes de utilizar el contenido en una cotización. |
|  **RN-12** | La plataforma deberá proporcionar mecanismos que permitan mejorar la experiencia digital de los clientes de SAMI. |
|  **RN-13** | El sistema deberá permitir que SAMI mantenga actualizada la información comercial de sus destinos y servicios. |
|  **RN-14** | La solución deberá permitir obtener información que facilite el seguimiento y análisis de las operaciones comerciales. |
|  **RN-15** | El sistema deberá proteger la información de clientes y usuarios mediante mecanismos de autenticación y control de acceso. |
|  **RN-16** | La solución deberá permitir que los procesos comerciales puedan continuar cuando alguno de los servicios externos integrados no esté disponible, siempre que exista un mecanismo alternativo. |

| ID | Requisito de negocio de agente IA |
| ----- | ----- |
| RN-IA-01 | SAMI deberá utilizar inteligencia artificial como herramienta de apoyo para reducir el tiempo requerido para elaborar itinerarios turísticos. |
| RN-IA-02 | La solución deberá utilizar IA para generar propuestas de itinerarios basadas en la información registrada en una cotización. |
| RN-IA-03 | La utilización de IA deberá mejorar la productividad del personal encargado de elaborar cotizaciones. |
| RN-IA-04 | La IA deberá funcionar como herramienta de asistencia y no sustituir la decisión final del agente de viajes. |
| RN-IA-05 | El contenido generado mediante IA deberá poder ser revisado y modificado antes de ser presentado al cliente. |
| RN-IA-06 | SAMI deberá mantener control sobre la información comercial utilizada en la cotización, independientemente del contenido generado por IA. |
| RN-IA-07 | El sistema deberá proporcionar mecanismos alternativos para continuar la elaboración de una cotización cuando el servicio de IA no esté disponible. |

- **Usuario:**

**Sami Travel & Tours** entiende que es lo que tiene que hacer el usuario para ser uso del sitio web, el sistema toma en cuenta los requisitos que necesita el usuario para tener una experiencia satisfactoria, por ejemplo: comprende la **interfaz de usuario,** quien es un **visitante**, **un cliente potencial (cliente registrado)**, **usuario de agente de viaje (asesor)** y **usuario administrador**.

| ID | Requisito de usuario |
| ----- | ----- |
|  **RU-B2C-01** | El visitante deberá poder consultar los servicios turísticos ofrecidos por SAMI sin necesidad de registrarse. |
|  **RU-B2C-02** | El visitante deberá poder explorar diferentes destinos turísticos. |
|  **RU-B2C-03** | El visitante deberá poder consultar información detallada de un destino. |
|  **RU-B2C-04** | El visitante deberá poder consultar paquetes vacacionales disponibles. |
|  **RU-B2C-05** | El visitante deberá poder buscar servicios o destinos de interés. |
|  **RU-B2C-06** | El visitante deberá poder solicitar información o una cotización. |
|  **RU-B2C-07** | El visitante deberá poder consultar los diferentes medios de contacto de SAMI. |
|  **RU-B2C-08** | El visitante deberá poder acceder al portal desde dispositivos móviles. |
|  **RU-B2C-09** | El visitante deberá poder consultar determinados contenidos previamente disponibles cuando no tenga conexión a Internet. |
|  **RU-B2C-10** | El visitante deberá poder instalar el portal como una aplicación web progresiva cuando su dispositivo sea compatible. |

| ID | Requisito de usuario potencial |
| ----- | ----- |
| **RU-CLI-01** | El cliente deberá poder registrarse en la plataforma. |
| **RU-CLI-02** | El cliente deberá poder autenticarse de forma segura. |
| **RU-CLI-03** | El cliente deberá poder consultar sus cotizaciones disponibles. |
| **RU-CLI-04** | El cliente deberá poder consultar el detalle de una cotización. |
| **RU-CLI-05** | El cliente deberá poder revisar el itinerario asociado a una cotización. |
| **RU-CLI-06** | El cliente deberá poder aprobar digitalmente una cotización cuando esta opción esté habilitada. |
| **RU-CLI-07** | El cliente deberá poder consultar el estado de sus solicitudes o cotizaciones. |
| **RU-CLI-08** | El cliente deberá poder actualizar determinados datos de su perfil. |
| **RU-CLI-09** | El cliente deberá poder cerrar su sesión de forma segura. |

| ID | Requisito de agente de viajes |
| ----- | ----- |
| **RU-CRM-01** | El agente deberá poder consultar y gestionar clientes desde el CRM. |
| **RU-CRM-02** | El agente deberá poder registrar nuevos clientes. |
| **RU-CRM-03** | El agente deberá poder crear y administrar cotizaciones. |
| **RU-CRM-04** | El agente deberá poder seleccionar destinos y servicios para una cotización. |
| **RU-CRM-05** | El agente deberá poder solicitar a la IA la generación de un itinerario. |
| **RU-CRM-06** | El agente deberá poder revisar y modificar el itinerario generado por IA. |
| **RU-CRM-07** | El agente deberá poder aprobar el contenido del itinerario antes de incorporarlo a la cotización. |
| **RU-CRM-08** | El agente deberá poder generar una cotización en formato PDF. |
| **RU-CRM-09** | El agente deberá poder consultar el historial de cotizaciones de un cliente. |
| **RU-CRM-10** | El agente deberá poder actualizar el estado de una oportunidad o cotización. |
| **RU-CRM-11** | El agente deberá poder consultar el tablero Kanban para visualizar el estado de sus oportunidades comerciales. |
| **RU-CRM-12** | El agente deberá poder consultar el catálogo de destinos y servicios disponibles. |

| ID | Requisito de Administrador |
| ----- | ----- |
| **RU-ADM-01** | El administrador deberá poder gestionar usuarios del sistema. |
| **RU-ADM-02** | El administrador deberá poder asignar roles y permisos. |
| **RU-ADM-03** | El administrador deberá poder gestionar destinos turísticos. |
| **RU-ADM-04** | El administrador deberá poder gestionar paquetes y servicios turísticos. |
| **RU-ADM-05** | El administrador deberá poder consultar registros de actividad relevantes del sistema. |
| **RU-ADM-06** | El administrador deberá poder configurar determinados parámetros del sistema. |
| **RU-ADM-07** | El administrador deberá poder tener acceso a configuración y creación de campañas. |

- **Requisitos Funcionales:**


| ID | Requisito funcional del Sistema |
| ----- | ----- |
| RF-B2C-01 | El sistema deberá mostrar una página principal con información general de SAMI Travels & Tours. |
| RF-B2C-02 | El sistema deberá mostrar el catálogo de destinos turísticos publicados. |
| RF-B2C-03 | El sistema deberá permitir consultar el detalle de cada destino. |
| RF-B2C-04 | El sistema deberá mostrar los paquetes turísticos publicados. |
| RF-B2C-05 | El sistema deberá permitir consultar el detalle de cada paquete. |
| RF-B2C-06 | El sistema deberá permitir buscar destinos y paquetes mediante palabras clave. |
| RF-B2C-07 | El sistema deberá permitir filtrar los resultados disponibles mediante criterios definidos por SAMI. |
| RF-B2C-08 | El sistema deberá mostrar información de contacto de SAMI. |
| RF-B2C-09 | El sistema deberá permitir al visitante iniciar una solicitud de cotización. |
| RF-B2C-10 | El sistema deberá registrar las solicitudes de información o cotización enviadas desde el portal. |
| RF-B2C-11 | El sistema deberá mostrar un mensaje de confirmación después del envío exitoso de una solicitud. |
| RF-B2C-12 | El sistema deberá proporcionar los recursos necesarios para funcionar como PWA. |
| RF-B2C-13 | El sistema deberá almacenar localmente los recursos definidos para funcionamiento offline. |
| RF-B2C-14 | El sistema deberá detectar el estado de conexión del dispositivo. |
| RF-B2C-15 | El sistema deberá actualizar los recursos almacenados cuando vuelva a existir conexión. |


- **Requisitos NO Funcionales:**

**3\. Historias de usuario y criterios de aceptación**   
 

| ID | Historia de usuario | Criterios de aceptación |
| :---- | :---- | :---- |
| HU-1 | Como cliente, quiero consultar los destinos, paquetes y servicios turísticos disponibles, para conocer las diferentes opciones antes de solicitar una cotización.   | 1\. El sistema debe mostrar los destinos, paquetes y servicios disponibles.  2\. El cliente debe poder consultar la información de cada opción.  3\. La información mostrada debe corresponder a los datos actualizados por SAMI.  4\. Los servicios no disponibles no deben presentarse como disponibles.   |
| HU-2 | Como cliente, quiero consultar las tarifas de viajes y tours, para conocer los costos antes de solicitar una cotización.   | 1\. El sistema debe mostrar las tarifas disponibles.  2\. Cada tarifa debe estar relacionada con el viaje o tour correspondiente.  3\. La información presentada debe coincidir con los datos registrados por SAMI.   |
| HU-3 | Como cliente, quiero recibir recomendaciones de viaje de acuerdo con mi presupuesto, para encontrar opciones que se adapten a mis necesidades y posibilidades.   | 1\. El cliente debe poder proporcionar información relacionada con su presupuesto.  2\. Las recomendaciones deben considerar la información proporcionada. 3\. Las recomendaciones deben corresponder a las opciones disponibles. 4\. El cliente debe poder consultar la información de las opciones recomendadas.   |
| HU-4 | Como cliente, quiero solicitar una cotización indicando las características de mi viaje, para recibir una propuesta acorde con mis necesidades.   | 1\. El cliente debe poder proporcionar la información necesaria de su viaje.  2\. Debe poder indicar la fecha y las opciones requeridas para la cotización. 3\. El sistema debe registrar correctamente la solicitud.  4\. El cliente debe recibir una confirmación de que su solicitud fue registrada.   |
| HU-5 | Como Agente de viajes, quiero gestionar las solicitudes y cotizaciones de los clientes, para dar seguimiento al proceso comercial de forma organizada.   | 1\. El personal autorizado debe poder consultar las solicitudes registradas.  2\. Debe poder dar seguimiento al estado de cada solicitud y cotización.  3\. La información de clientes, servicios y cotizaciones debe encontrarse centralizada.  4\. Los cambios realizados deben quedar registrados correctamente.   |
| HU-6 | Como Agente de viajes, quiero elaborar cotizaciones con la información del cliente y los servicios seleccionados, para entregar propuestas de viaje claras y organizadas.   | 1\. El personal autorizado debe poder seleccionar la información necesaria para elaborar la cotización. 2\. La cotización debe incluir los servicios y datos correspondientes al viaje solicitado. 3\. El sistema debe permitir generar un documento de cotización. 4\. La información debe poder revisarse antes de entregar la cotización al cliente. |
| HU-7 | Como Agente de viajes, quiero obtener una propuesta inicial de itinerario con apoyo de inteligencia artificial, para reducir el tiempo necesario para preparar una cotización.     | 1\. El sistema debe permitir generar una propuesta de itinerario a partir de la información disponible del viaje.  2\. El contenido generado debe poder ser revisado por personal autorizado.  3\. El itinerario no debe incorporarse a una cotización sin haber sido revisado y aprobado.  4\. El personal debe poder realizar ajustes antes de utilizar la propuesta.   |
| HU-8 | Como usuario registrado, quiero acceder de forma segura a la plataforma, para consultar y gestionar únicamente la información que me corresponde.     | 1\. El sistema debe solicitar autenticación para acceder a las funciones restringidas.  2\. Solo los usuarios autorizados deben acceder a información protegida.  3\. Las funciones disponibles deben depender del tipo de usuario.  4\. Los usuarios no autorizados no deben acceder a información restringida.   |

**4\. Casos de uso y diagrama de casos de uso** 

Los casos de uso permiten representar las principales interacciones entre los usuarios y la plataforma de SAMI Travels & Tours. Para su elaboración se tomaron en cuenta los requisitos y las historias de usuario previamente establecidas, considerando como actores principales al cliente potencial, agente de viajes y administrador.

