"""Question bank: 2 questions per topic (80 total). No LLM dependency."""

SEED_QUESTIONS = [
    # =====================================================================
    # TEMA 1 - Constitucion Espanola 1978: Estructura, Titulo Preliminar, Titulo I, Titulo III
    # =====================================================================
    {
        "topic_num": 1,
        "question": "Segun la Constitucion Espanola de 1978, cual de los siguientes derechos fundamentales esta recogido en el Titulo I?",
        "option_a": "El derecho a la propiedad industrial exclusiva",
        "option_b": "El derecho a la vida y a la integridad fisica (art. 15)",
        "option_c": "El derecho a la jubilacion anticipada universal",
        "option_d": "El derecho a la libre competencia economica ilimitada",
        "correct": "B",
        "explanation": "El art. 15 CE reconoce el derecho a la vida y a la integridad fisica y moral, sin que en ningun caso pueda nadie ser sometido a torturas ni a penas o tratos inhumanos o degradantes."
    },
    {
        "topic_num": 1,
        "question": "Cuantos Titulos componen la estructura de la Constitucion Espanola de 1978?",
        "option_a": "8 Titulos",
        "option_b": "9 Titulos, mas Titulo Preliminar y Disposiciones",
        "option_c": "10 Titulos",
        "option_d": "7 Titulos y un Preliminar",
        "correct": "B",
        "explanation": "La CE de 1978 se estructura en Titulo Preliminar, 10 Titulos (I a X) y Disposiciones Adicionales, Transitorias, Derogatorias y Final."
    },

    # =====================================================================
    # TEMA 2 - Constitucion Espanola 1978: Titulo IV, Titulo V, Titulo VIII
    # =====================================================================
    {
        "topic_num": 2,
        "question": "Segun el Titulo IV de la CE, quien preside el Gobierno de la Nacion?",
        "option_a": "El Rey",
        "option_b": "El Presidente del Congreso de los Diputados",
        "option_c": "El Presidente del Gobierno",
        "option_d": "El Vicepresidente primero",
        "correct": "C",
        "explanation": "El art. 98 CE establece que el Gobierno esta compuesto por el Presidente, los Vicepresidentes, en su caso, los Ministros y los demas miembros que establezca la ley. Corresponde al Presidente del Gobierno la direccion de la politica interior y exterior."
    },
    {
        "topic_num": 2,
        "question": "El Titulo VIII de la Constitucion se refiere principalmente a:",
        "option_a": "La organizacion territorial del Estado",
        "option_b": "El poder judicial",
        "option_c": "Las Cortes Generales",
        "option_d": "La Corona",
        "correct": "A",
        "explanation": "El Titulo VIII (arts 143 a 158) regula la Organizacion Territorial del Estado, reconociendo la autonomia de las nacionalidades y regiones que integran Espana."
    },

    # =====================================================================
    # TEMA 3 - Ley 7/1985 Bases Regimen Local: Municipio y Provincia
    # =====================================================================
    {
        "topic_num": 3,
        "question": "Segun la Ley 7/1985, de Bases del Regimen Local, cual es el organo de gobierno municipal?",
        "option_a": "El Pleno unicamente",
        "option_b": "La Alcaldia o Junta de Gobierno Local",
        "option_c": "El Secretario del Ayuntamiento",
        "option_d": "El Interventor",
        "correct": "B",
        "explanation": "El art. 21 LRBL establece que el gobierno y la administracion municipal corresponden a la Alcaldia, integrada por el Alcalde y los Tenientes de Alcalde, o a la Junta de Gobierno Local en municipios de poblacion superior a 5.000 habitantes."
    },
    {
        "topic_num": 3,
        "question": "En la organizacion provincial segun la Ley 7/1985, quien ejerce la presidencia de la Diputacion?",
        "option_a": "El Delegado del Gobierno",
        "option_b": "El Presidente elegido por los Diputados provinciales",
        "option_c": "El Alcalde del municipio de mayor poblacion",
        "option_d": "El Secretario Provincial",
        "correct": "B",
        "explanation": "El art. 31 LRBL establece que la Diputacion esta constituida por el Presidente, la Vicepresidencia, la Junta Provincial y los Diputados, siendo el Presidente elegido por los Diputados entre sus miembros."
    },

    # =====================================================================
    # TEMA 4 - RDL 781/1986 Regimen Local. RD 2568/1986 Reglamento
    # =====================================================================
    {
        "topic_num": 4,
        "question": "El Real Decreto Legislativo 781/1986 aprueba el texto refundido de disposiciones legales vigentes en materia de:",
        "option_a": "Funcion Publica",
        "option_b": "Regimen Local",
        "option_c": "Contratos del Sector Publico",
        "option_d": "Procedimiento Administrativo",
        "correct": "B",
        "explanation": "El RDL 781/1986 aprueba el Texto Refundido de las disposiciones legales vigentes en materia de Regimen Local, recogiendo la LRBL y otras normas complementarias."
    },
    {
        "topic_num": 4,
        "question": "Segun el RD 2568/1986, a que organo corresponde la funcion de fiscalizacion interna en las Entidades Locales?",
        "option_a": "Al Pleno",
        "option_b": "A la Intervencion",
        "option_c": "Al Secretario",
        "option_d": "A la Junta de Gobierno",
        "correct": "B",
        "explanation": "La Intervencion General u organo de fiscalizacion interna ejerce el control interno de la gestion economico-financiera, segun el Titulo II del RD 2568/1986."
    },

    # =====================================================================
    # TEMA 5 - Ley 39/2015 LPACAP: Disposiciones generales, Interesados
    # =====================================================================
    {
        "topic_num": 5,
        "question": "Segun la Ley 39/2015, que plazo maximo tienen las Administraciones Publicas para resolver y notificar los procedimientos administrativos?",
        "option_a": "1 mes",
        "option_b": "3 meses (art. 42.1 LPACAP)",
        "option_c": "6 meses",
        "option_d": "12 meses",
        "correct": "B",
        "explanation": "El art. 42.1 LPACAP establece que el plazo maximo para resolver y notificar es de 3 meses, salvo que una norma con rango de ley establezca otro plazo."
    },
    {
        "topic_num": 5,
        "question": "En la LPACAP, la capacidad de obrar de los menores de edad en el ambito administrativo se reconoce a partir de:",
        "option_a": "Los 14 anos",
        "option_b": "Los 16 anos",
        "option_c": "Los 18 anos",
        "option_d": "Los 12 anos",
        "correct": "B",
        "explanation": "El art. 3.3 LPACAP establece que tienen capacidad para ser parte e interesados en el procedimiento administrativo quienes hayan cumplido los dieciséis anos."
    },

    # =====================================================================
    # TEMA 6 - Ley 39/2015 LPACAP: Actividad admin, Actos administrativos
    # =====================================================================
    {
        "topic_num": 6,
        "question": "Segun la LPACAP, un acto administrativo vencido en su plazo de recurso y que no ha sido impugnado se denomina:",
        "option_a": "Acto nulo",
        "option_b": "Acto firme en via administrativa",
        "option_c": "Acto anulable",
        "option_d": "Acto provision",
        "correct": "B",
        "explanation": "El art. 51 LPACAP establece que la firmeza en via administrativa se produce cuando el acto no ha sido impugnado en el plazo establecido, o cuando se ha desestimado el recurso."
    },
    {
        "topic_num": 6,
        "question": "La nulidad de pleno derecho de los actos administrativos (art. 47 LPACAP) afecta a actos que:",
        "option_a": "Solo incurran en error de hecho",
        "option_b": "Vulneren la Constitucion, las leyes u otros derechos y libertades publicas",
        "option_c": "Carezcan de motivacion extendida",
        "option_d": "Hayan sido dictados fuera del horario de oficina",
        "correct": "B",
        "explanation": "El art. 47.1 LPACAP declara nulos de pleno derecho los actos que infrinjan la Constitucion, la ley o cualquier otra disposicion de rango legal, o lesionen derechos y libertades publicas."
    },

    # =====================================================================
    # TEMA 7 - Ley 31/1995 Prevencion de Riesgos Laborales
    # =====================================================================
    {
        "topic_num": 7,
        "question": "Segun la Ley 31/1995 de Prevencion de Riesgos Laborales, los principios de la accion preventiva incluyen:",
        "option_a": "Evitar los riesgos, evaluar los que no se puedan evitar y combatirlos en su origen",
        "option_b": "Solo informar al trabajador de los riesgos existentes",
        "option_c": "Delegar la prevencion exclusivamente en las mutuas de accidentes",
        "option_d": "Realizar controles medicos anuales gratuitos unicamente",
        "correct": "A",
        "explanation": "El art. 15 LPRL establece principios preventivos: evitar riesgos, evaluar los inevitables, combatir en origen, adaptar trabajo a persona, tener en cuenta la evolucion de la tecnica, sustituir lo peligroso por lo seguro, planificar la prevencion, aplicar medidas coherentes y dar prioridad a protecciones colectivas."
    },
    {
        "topic_num": 7,
        "question": "La evaluacion de riesgos obligatoria segun la LPRL debe ser realizada por:",
        "option_a": "Solo el Servicio de Prevencion Ajeno",
        "option_b": "El empresario, que puede realizarla directamente o mediante servicios de prevencion",
        "option_c": "Exclusivamente la Inspeccion de Trabajo",
        "option_d": "El comite de empresa unicamente",
        "correct": "B",
        "explanation": "El art. 14 LPRL impone al empresario la obligacion de evaluar los riesgos, pudiendo realizarla directamente, mediante servicio de prevencion propio o ajeno."
    },

    # =====================================================================
    # TEMA 8 - Legislacion basica sobre igualdad
    # =====================================================================
    {
        "topic_num": 8,
        "question": "La Ley Organica 3/2007, de igualdad efectiva de mujeres y hombres, establece que las Administraciones Publicas deben promover la igualdad mediante:",
        "option_a": "La prohibicion expresa de la contratacion femenina en ciertos sectores",
        "option_b": "La integracion del principio de igualdad en la planificacion presupuestaria y evaluacion de politicas publicas",
        "option_c": "La reduccion de la jornada laboral exclusiva para mujeres",
        "option_d": "La cuota de genero del 60% en todos los organos publicos",
        "correct": "B",
        "explanation": "El art. 15 LO 3/2007 establece la transversalidad de la igualdad en las politicas publicas, incluyendo la incorporacion del principio en la planificacion presupuestaria (presupuestos con perspectiva de genero)."
    },
    {
        "topic_num": 8,
        "question": "Segun la Ley 4/2018 de Castilla-La Mancha para una Sociedad Libre de Violencia de Genero, la violencia de genero se entiende como:",
        "option_a": "Cualquier altercado domestico ocasional",
        "option_b": "Cualquier acto de violencia fisica, psicologica o sexual contra una mujer por el mero hecho de serlo, o que afecte desproporcionadamente a mujeres",
        "option_c": "Solo los delitos de lesiones en el ambito familiar",
        "option_d": "La discriminacion laboral por razon de sexo",
        "correct": "B",
        "explanation": "El Art. 1 Ley 4/2018 CLM define la violencia de genero como cualquier acto de violencia fisica, psicologica o sexual contra las mujeres por el mero hecho de serlo, incluyendo todo tipo de violencia que afecte desproporcionadamente a mujeres."
    },

    # =====================================================================
    # TEMA 9 - Firma electronica
    # =====================================================================
    {
        "topic_num": 9,
        "question": "Segun el Reglamento eIDAS, la firma electronica avanzada debe permitir:",
        "option_a": "La identificacion del signatario y detectar cualquier cambio posterior en los datos firmados",
        "option_b": "Solo la identificacion del documento firmado",
        "option_c": "La encriptacion completa del documento",
        "option_d": "La firma simultanea por varios signatarios sin identificacion",
        "correct": "A",
        "explanation": "El Reglamento eIDAS (UE) 910/2014 define la firma electronica avanzada como aquella que permite identificar al signatario y detectar cualquier cambio posterior de los datos firmados, vinculada de forma unica al signatario y bajo su control exclusivo."
    },
    {
        "topic_num": 9,
        "question": "La aplicacion de firma electronica @firma del MINHAP permite:",
        "option_a": "Verificar y validar firmas electronicas de cualquier tipo conforme al Esquema Nacional de Seguridad",
        "option_b": "Solo firmar documentos con certificados de la FNMT",
        "option_c": "Cifrar archivos usando AES-256 exclusivamente",
        "option_d": "Gestionar unicamente firmas PAdES en formato PDF",
        "correct": "A",
        "explanation": "@firma es la plataforma del MINHAP que proporciona servicios de firma y validacion de firmas electronicas, admitiendo multiples formatos (XAdES, CAdES, PAdES) y cumpliendo con el ENS."
    },

    # =====================================================================
    # TEMA 10 - Cifrado, PKI, SSL/TLS, PGP
    # =====================================================================
    {
        "topic_num": 10,
        "question": "En una Infraestructura de Clave Publica (PKI), que funcion cumple la Autoridad de Certificacion (CA)?",
        "option_a": "Almacenar los datos cifrados de los usuarios",
        "option_b": "Emitir, revocar y gestionar certificados digitales que vinculan una clave publica con la identidad de un sujeto",
        "option_c": "Generar claves privadas para todos los usuarios",
        "option_d": "Descifrar mensajes entre usuarios",
        "correct": "B",
        "explanation": "La CA es el elemento central de una PKI que actua como tercero de confianza, emitiendo certificados tras verificar la identidad del solicitante y manteniendo listas de revocacion (CRL)."
    },
    {
        "topic_num": 10,
        "question": "En el protocolo TLS (Transport Layer Security), que fase se encarga de acordar los parametros criptograficos entre cliente y servidor?",
        "option_a": "La fase de handshake",
        "option_b": "La fase de transferencia de datos",
        "option_c": "La fase de cierre de conexion",
        "option_d": "La fase de renegociacion",
        "correct": "A",
        "explanation": "El handshake TLS es el proceso inicial en el que cliente y servidor acuerdan la version del protocolo, suite criptografica, intercambian claves y autentican identidades mediante certificados."
    },

    # =====================================================================
    # TEMA 11 - Esquema Nacional de Seguridad
    # =====================================================================
    {
        "topic_num": 11,
        "question": "El Esquema Nacional de Seguridad (Real Decreto 311/2022) clasifica los sistemas segun su criticidad en:",
        "option_a": "Solo dos niveles: basico y alto",
        "option_b": "Tres categorias: bajo, medio y alto, cada uno con un conjunto de medidas obligatorias",
        "option_c": "Cinco niveles numericos del 1 al 5",
        "option_d": "Ninguna clasificacion, todas las medidas son opcionales",
        "correct": "B",
        "explanation": "El ENS establece tres categorias (bajo, medio, alto) definiendo medidas de seguridad proporcionales a la criticidad. Cada categoria incluye medidas obligatorias del Esquema Nacional y de cada organismo."
    },
    {
        "topic_num": 11,
        "question": "Segun el ENS, los principios basicos de seguridad de la informacion incluyen:",
        "option_a": "Solo confidencialidad y disponibilidad",
        "option_b": "Confidencialidad, integridad, trazabilidad, autenticidad y disponibilidad",
        "option_c": "Velocidad, escalabilidad y redundancia",
        "option_d": "Usabilidad, accesibilidad y rendimiento",
        "correct": "B",
        "explanation": "El Anexo I del ENS establece los principios basicos: confidencialidad, integridad, trazabilidad, autenticidad y disponibilidad. Estos principios orientan la seleccion y aplicacion de medidas de seguridad."
    },

    # =====================================================================
    # TEMA 12 - Proteccion de datos
    # =====================================================================
    {
        "topic_num": 12,
        "question": "Segun el RGPD, el responsable del tratamiento debe informar al interesado sobre el tratamiento de sus datos en el momento de:",
        "option_a": "Solo cuando el interesado lo solicite expresamente",
        "option_b": "La obtencion de los datos, con caracter previo (principio de transparencia, art. 13)",
        "option_c": "Un mes despues de la obtencion de los datos",
        "option_d": "Unicamente cuando haya una filtracion de seguridad",
        "correct": "B",
        "explanation": "El art. 12 y 13 RGPD establecen el deber de informacion cuando los datos se obtienen del interesado, proporcionandola de forma concisa, transparente, inteligible y facilmente accesible."
    },
    {
        "topic_num": 12,
        "question": "En materia de proteccion de datos, la LOPDGDD (Ley Organica 3/2018) desarrolla aspectos del RGPD relativos a:",
        "option_a": "La regulacion exclusiva de datos sanitarios",
        "option_b": "Derechos digitales, edad de consentimiento (14 anos), y regimen sancionador en Espana",
        "option_c": "Solo la creacion de la AEPD",
        "option_d": "La proteccion de datos de empresas unicamente",
        "correct": "B",
        "explanation": "La LOPDGDD desarrolla el RGPD en aspectos como: derechos digitales, edad de consentimiento (14 anos), tratamiento de datos de menores, representacion, deberes del delegado de proteccion de datos y regimen sancionador."
    },

    # =====================================================================
    # TEMA 13 - PostgreSQL: Arquitectura de servidor
    # =====================================================================
    {
        "topic_num": 13,
        "question": "En la arquitectura de PostgreSQL, que proceso principal escucha conexiones entrantes y gestiona los backends?",
        "option_a": "El proceso WAL writer",
        "option_b": "El postmaster",
        "option_c": "El autovacuum launcher",
        "option_d": "El background writer",
        "correct": "B",
        "explanation": "El postmaster es el proceso principal del servidor PostgreSQL que escucha en el puerto configurado (por defecto 5432), acepta conexiones de clientes y genera un proceso backend dedicado para cada conexion."
    },
    {
        "topic_num": 13,
        "question": "Para garantizar la durabilidad (D de ACID), PostgreSQL utiliza principalmente:",
        "option_a": "Solo memoria compartida (shared_buffers)",
        "option_b": "Escritura previa de registro (WAL - Write Ahead Logging)",
        "option_c": "Solo indices B-tree",
        "option_d": "Tablas temporales en disco",
        "correct": "B",
        "explanation": "PostgreSQL utiliza WAL para garantizar durabilidad: antes de modificar los datos en disco, se escribe un registro en el WAL. Esto permite recuperar la base de datos tras un crash."
    },

    # =====================================================================
    # TEMA 14 - PostgreSQL: Jerarquia de objetos y funciones
    # =====================================================================
    {
        "topic_num": 14,
        "question": "En PostgreSQL, cual es la jerarquia correcta de contencion de objetos?",
        "option_a": "Cluster > Base de datos > Esquema > Tabla",
        "option_b": "Base de datos > Cluster > Esquema > Tabla",
        "option_c": "Esquema > Base de datos > Tabla > Columna",
        "option_d": "Tabla > Esquema > Base de datos > Cluster",
        "correct": "A",
        "explanation": "La jerarquia en PostgreSQL es: Cluster (instancia del servidor) contiene multiples bases de datos. Cada base de datos contiene esquemas. Cada esquema contiene tablas, vistas, funciones, etc."
    },
    {
        "topic_num": 14,
        "question": "En PostgreSQL, que tipo de objeto permite ejecutar codigo procedural (PL/pgSQL) como parte del modelo relacional?",
        "option_a": "Solo las tablas",
        "option_b": "Las funciones (CREATE FUNCTION / CREATE OR REPLACE FUNCTION)",
        "option_c": "Los indices",
        "option_d": "Los tablespaces",
        "correct": "B",
        "explanation": "Las funciones en PostgreSQL permiten encapsular logica procedural usando PL/pgSQL u otros lenguajes. Se invocan directamente en consultas, triggers o procedimientos almacenados."
    },

    # =====================================================================
    # TEMA 15 - PostgreSQL: Transacciones
    # =====================================================================
    {
        "topic_num": 15,
        "question": "En PostgreSQL, el nivel de aislamiento por defecto de una transaccion es:",
        "option_a": "READ COMMITTED",
        "option_b": "REPEATABLE READ",
        "option_c": "SERIALIZABLE",
        "option_d": "READ UNCOMMITTED",
        "correct": "A",
        "explanation": "PostgreSQL utiliza READ COMMITTED como nivel de aislamiento por defecto. En este nivel, una consulta dentro de una transaccion solo ve datos confirmados antes de que la consulta comience."
    },
    {
        "topic_num": 15,
        "question": "Las propiedades ACID de una transaccion se refieren a:",
        "option_a": "Atomicidad, Consistencia, Aislamiento, Durabilidad",
        "option_b": "Accesibilidad, Concurrencia, Integridad, Disponibilidad",
        "option_c": "Autenticacion, Cifrado, Integridad, Depuracion",
        "option_d": "Asincronia, Cacheo, Indexacion, Distribucion",
        "correct": "A",
        "explanation": "ACID significa Atomicidad (todo o nada), Consistencia (el estado valido se mantiene), Aislamiento (transacciones concurrentes no se interfieren) y Durabilidad (los cambios persisten tras commit)."
    },

    # =====================================================================
    # TEMA 16 - PostgreSQL: Herramientas cliente, import/export
    # =====================================================================
    {
        "topic_num": 16,
        "question": "Que herramienta de PostgreSQL se utiliza para realizar copias de seguridad logicas de una base de datos?",
        "option_a": "pg_ctl",
        "option_b": "pg_dump",
        "option_c": "psql",
        "option_d": "pg_waldump",
        "correct": "B",
        "explanation": "pg_dump es la herramienta estandar para realizar backups logicos. Genera un archivo SQL o en formato custom que puede restaurarse con pg_restore."
    },
    {
        "topic_num": 16,
        "question": "Para importar datos masivamente desde un archivo CSV en PostgreSQL, el metodo mas eficiente es:",
        "option_a": "INSERT INTO ... SELECT * FROM un archivo",
        "option_b": "La sentencia COPY o \\copy en psql",
        "option_c": "Crear una funcion PL/pgSQL que lea linea a linea",
        "option_d": "Usar pg_dump en modo restore",
        "correct": "B",
        "explanation": "COPY es la forma mas rapida de importar/exportar datos tabulares en PostgreSQL, ya que opera a nivel de servidor sin overhead de SQL parseado fila a fila."
    },

    # =====================================================================
    # TEMA 17 - PostgreSQL: Optimizacion
    # =====================================================================
    {
        "topic_num": 17,
        "question": "En PostgreSQL, que comando se utiliza para obtener un plan de ejecucion detallado de una consulta incluyendo tiempos reales?",
        "option_a": "SHOW PLAN",
        "option_b": "EXPLAIN ANALYZE",
        "option_c": "DESCRIBE QUERY",
        "option_d": "PROFILE SQL",
        "correct": "B",
        "explanation": "EXPLAIN ANALYZE ejecuta la consulta y muestra el plan de ejecucion con tiempos y filas reales procesadas, siendo la herramienta fundamental para el tuning de rendimiento."
    },
    {
        "topic_num": 17,
        "question": "La operacion VACUUM en PostgreSQL se utiliza principalmente para:",
        "option_a": "Cifrar las tablas sensibles",
        "option_b": "Recuperar espacio de filas eliminadas o actualizadas y prevenir el swell de tablas",
        "option_c": "Compactar los indices automaticamente",
        "option_d": "Backup incremental de la base de datos",
        "correct": "B",
        "explanation": "PostgreSQL utiliza MVCC, por lo que las actualizaciones/eliminaciones dejan tuplas muertas. VACUUM marca estas tuplas como reutilizables. VACUUM FULL reescribe fisicamente las tablas para devolver espacio al SO."
    },

    # =====================================================================
    # TEMA 18 - Fundamentos de programacion C#
    # =====================================================================
    {
        "topic_num": 18,
        "question": "En C#, que palabra clave se utiliza para declarar un tipo de valor que puede contener nulos?",
        "option_a": "object",
        "option_b": "nullable o el operador ? tras el tipo (int?)",
        "option_c": "var",
        "option_d": "dynamic",
        "correct": "B",
        "explanation": "Los tipos valor no aceptan null por defecto. Se usa Nullable<T> o la sintaxis T? (ej. int?) para permitir nulos en tipos de valor desde C# 2.0."
    },
    {
        "topic_num": 18,
        "question": "En C#, la diferencia fundamental entre una clase (class) y una estructura (struct) es que:",
        "option_a": "Las clases solo pueden tener metodos estaticos",
        "option_b": "Las clases son tipos referencia (almacenadas en heap) y las estructuras son tipos valor (almacenadas en stack)",
        "option_c": "Las estructuras no pueden tener constructores",
        "option_d": "Las clases solo existen en .NET Framework, no en .NET Core",
        "correct": "B",
        "explanation": "En C#, class define un tipo referencia (asignacion copia la referencia, no el objeto), mientras que struct define un tipo valor (asignacion copia el valor completo). Esto afecta rendimiento y semantica."
    },

    # =====================================================================
    # TEMA 19 - Construccion de sitios web con MVC. Bootstrap
    # =====================================================================
    {
        "topic_num": 19,
        "question": "En ASP.NET Core MVC, que componente recibe las peticiones HTTP, ejecuta la logica de negocio y selecciona la vista a renderizar?",
        "option_a": "El Modelo",
        "option_b": "El Controller",
        "option_c": "La Vista",
        "option_d": "El Middleware",
        "correct": "B",
        "explanation": "El Controller es el componente C del patron MVC. Recibe peticiones, trabaja con los modelos y decide que vista presentar, pasandole los datos necesarios (ViewModel)."
    },
    {
        "topic_num": 19,
        "question": "Bootstrap es un framework CSS que proporciona principalmente:",
        "option_a": "Un motor de base de datos ligero",
        "option_b": "Un sistema de rejilla responsive, componentes de UI predefinidos y utilidades CSS",
        "option_c": "Un lenguaje de programacion para el frontend",
        "option_d": "Un servidor web embebido",
        "correct": "B",
        "explanation": "Bootstrap es un framework frontend que incluye un sistema de grid responsive basado en flexbox, componentes (navegacion, forms, tablas, modales) y utilidades de espaciado, colores y tipografia."
    },

    # =====================================================================
    # TEMA 20 - Entity Framework Core
    # =====================================================================
    {
        "topic_num": 20,
        "question": "En Entity Framework Core, que clase principal actua como puente entre las entidades del dominio y la base de datos?",
        "option_a": "DbSet<T>",
        "option_b": "DbContext",
        "option_c": "IQueryable",
        "option_d": "SqlConnection",
        "correct": "B",
        "explanation": "DbContext es la clase central de EF Core que gestiona la conexion, el seguimiento de entidades (change tracking), las transacciones y la traduccion de consultas LINQ a SQL."
    },
    {
        "topic_num": 20,
        "question": "El comando `dotnet ef migrations add` en EF Core se utiliza para:",
        "option_a": "Compilar el proyecto",
        "option_b": "Crear un nuevo archivo de migracion basado en los cambios detectados en el modelo de datos",
        "option_c": "Conectar a la base de datos directamente",
        "option_d": "Eliminar todas las tablas existentes",
        "correct": "B",
        "explanation": "Las migraciones en EF Core permiten versionar el esquema de la base de datos. dotnet ef migrations add genera un archivo C# con las operaciones necesarias para actualizar el esquema (Up) o revertirlo (Down)."
    },

    # =====================================================================
    # TEMA 21 - LINQ
    # =====================================================================
    {
        "topic_num": 21,
        "question": "En LINQ, el metodo de extension `Where` se utiliza para:",
        "option_a": "Ordenar elementos",
        "option_b": "Filtrar elementos segun una condicion booleana (predicado)",
        "option_c": "Agrupar elementos por una clave",
        "option_d": "Proyectar cada elemento en un nuevo tipo",
        "correct": "B",
        "explanation": "Where aplica un filtro a una secuencia, devolviendo solo los elementos que cumplen el predicado. Es el equivalente a la clausula WHERE de SQL."
    },
    {
        "topic_num": 21,
        "question": "Que metodo LINQ se utiliza para proyectar cada elemento de una coleccion a un nuevo tipo o forma?",
        "option_a": "Aggregate",
        "option_b": "Select",
        "option_c": "Join",
        "option_d": "GroupBy",
        "correct": "B",
        "explanation": "Select proyecta cada elemento a un nuevo tipo (o anonimo). Es equivalente a SELECT en SQL. Puede transformar propiedades, crear objetos anonimos o calcular valores derivados."
    },

    # =====================================================================
    # TEMA 22 - Model binding, validacion, tareas asincronas
    # =====================================================================
    {
        "topic_num": 22,
        "question": "En ASP.NET Core MVC, el model binding es el proceso que:",
        "option_a": "Compila los modelos automaticamente desde la base de datos",
        "option_b": "Mapea datos de la peticion HTTP (formularios, query strings, JSON) a los parametros de accion del controlador o a las propiedades del modelo",
        "option_c": "Genera las vistas automaticamente para cada entidad",
        "option_d": "Cifra los datos de los modelos antes de enviarlos al cliente",
        "correct": "B",
        "explanation": "El model binding en ASP.NET Core convierte automaticamente los datos de la peticion (ruta, query, form, body, header) en objetos .NET que el controlador puede utilizar directamente."
    },
    {
        "topic_num": 22,
        "question": "En C# asincrono, la palabra clave `await` se utiliza para:",
        "option_a": "Detener permanentemente la ejecucion del programa",
        "option_b": "Suspender la ejecucion del metodo async hasta que la tarea completada sin bloquear el hilo",
        "option_c": "Eliminar automaticamente las excepciones",
        "option_d": "Forzar la ejecucion sincrona de un metodo",
        "correct": "B",
        "explanation": "await suspende la ejecucion del metodo async y devuelve el control al llamador sin bloquear el hilo. Cuando la tarea completa, la ejecucion continua desde el punto de suspension."
    },

    # =====================================================================
    # TEMA 23 - Autenticacion y autorizacion. Filtros
    # =====================================================================
    {
        "topic_num": 23,
        "question": "En ASP.NET Core, la diferencia entre autenticacion y autorizacion es que:",
        "option_a": "Son sinonimos y se usan indistintamente",
        "option_b": "La autenticacion identifica quien es el usuario; la autorizacion determina que puede hacer",
        "option_c": "La autenticacion controla el acceso a la base de datos; la autorizacion al frontend",
        "option_d": "La autenticacion usa solo cookies; la autorizacion solo tokens JWT",
        "correct": "B",
        "explanation": "Autenticacion = verificar la identidad del usuario (quien eres). Autorizacion = verificar permisos sobre recursos (que puedes hacer). Son procesos independientes pero secuenciales."
    },
    {
        "topic_num": 23,
        "question": "En ASP.NET Core MVC, los filtros de accion (Action Filters) se ejecutan:",
        "option_a": "Antes y despues de la ejecucion de un metodo de accion del controlador",
        "option_b": "Solo durante la fase de autorizacion",
        "option_c": "Unicamente al iniciar la aplicacion",
        "option_d": "Despues de que la vista ha sido renderizada",
        "correct": "A",
        "explanation": "Los Action Filters implementan IActionFilter, con OnActionExecuting (antes del metodo) y OnActionExecuted (despues). Permiten inyectar logica transversal como logging, validacion o transformacion de resultados."
    },

    # =====================================================================
    # TEMA 24 - Web API
    # =====================================================================
    {
        "topic_num": 24,
        "question": "Un controlador ASP.NET Core Web API habitualmente hereda de:",
        "option_a": "Controller",
        "option_b": "ControllerBase",
        "option_c": "ApiControllerBase",
        "option_d": "MvcController",
        "correct": "B",
        "explanation": "ControllerBase es la clase base para Web APIs (sin soporte de vistas). Controller hereda de ControllerBase y anade soporte para vistas Razor, siendo mas adecuado para MVC tradicional."
    },
    {
        "topic_num": 24,
        "question": "Segun las convenciones REST, que metodo HTTP se utiliza para actualizar parcialmente un recurso?",
        "option_a": "PUT",
        "option_b": "PATCH",
        "option_c": "POST",
        "option_d": "DELETE",
        "correct": "B",
        "explanation": "PATCH se usa para actualizaciones parciales (solo los campos enviados). PUT reemplaza el recurso completo. POST crea. DELETE elimina."
    },

    # =====================================================================
    # TEMA 25 - OData
    # =====================================================================
    {
        "topic_num": 25,
        "question": "OData es un estandar de protocolo que permite:",
        "option_a": "Solo el envio de datos en formato CSV",
        "option_b": "Consultar y manipular datos mediante operaciones CRUD sobre URLs RESTful usando formato estandarizado",
        "option_c": "La encriptacion punto a punto de servicios web",
        "option_d": "La migracion automatica de bases de datos",
        "correct": "B",
        "explanation": "OData (Open Data Protocol) es un estandar OASIS que define practicas para crear y consumir APIs RESTful de forma uniforme, usando convenciones de URL para filtros, ordenacion, paginacion y CRUD."
    },
    {
        "topic_num": 25,
        "question": "En OData, para filtrar recursos donde el precio sea mayor que 100, se utiliza el parametro de consulta:",
        "option_a": "$sort=price gt 100",
        "option_b": "$filter=price gt 100",
        "option_c": "$search=price>100",
        "option_d": "$where=price gt 100",
        "correct": "B",
        "explanation": "La opcion de sistema $filter en OData permite expresar predicados de filtrado usando operadores como eq, ne, gt, ge, lt, le, and, or, not."
    },

    # =====================================================================
    # TEMA 26 - Blazor: Modelos de alojamiento
    # =====================================================================
    {
        "topic_num": 26,
        "question": "Blazor es un framework de .NET para construir interfaces web interactivas que permite ejecutar:",
        "option_a": "Solo codigo JavaScript en el navegador",
        "option_b": "Codigo C# tanto en el servidor como directamente en el navegador via WebAssembly",
        "option_c": "Solo aplicaciones de escritorio Windows",
        "option_d": "Solo APIs REST en el backend",
        "correct": "B",
        "explanation": "Blazor ofrece dos modelos de hosting: Blazor Server (UI en servidor, comunicacion via SignalR) y Blazor WebAssembly (UI ejecuta en navegador via WebAssembly, sin conexion persistente al servidor)."
    },
    {
        "topic_num": 26,
        "question": "La principal desventaja de Blazor Server frente a Blazor WebAssembly es que:",
        "option_a": "Requiere un plugin instalado en el navegador",
        "option_b": "Mantiene una conexion persistente (SignalR) con el servidor y es mas sensible a la latencia de red",
        "option_c": "No soporta componentes Razor",
        "option_d": "No puede ejecutar codigo C#",
        "correct": "B",
        "explanation": "Blazor Server renderiza en servidor y envia actualizaciones de DOM via SignalR. Si la conexion se interrumpe, la UI deja de responder. Ademas, cada interaccion genera latencia de ida y vuelta."
    },

    # =====================================================================
    # TEMA 27 - Blazor: Componentes basicos, binding, parametros, cascada
    # =====================================================================
    {
        "topic_num": 27,
        "question": "En Blazor, el binding unidireccional (one-way) se expresa con la sintaxis:",
        "option_a": "@bind-variable",
        "option_b": "@variable",
        "option_c": "{{variable}}",
        "option_d": "${variable}",
        "correct": "B",
        "explanation": "En Razor/Blazor, @variable renderiza el valor en la UI. El two-way binding usa @bind='variable' para sincronizar valor y evento de cambio."
    },
    {
        "topic_num": 27,
        "question": "En Blazor, los CascadingValue/CascadingParameter permiten:",
        "option_a": "Enviar datos desde un componente ancestro a todos sus descendientes sin pasar por parametros intermedios",
        "option_b": "Guardar datos en la base de datos local del navegador",
        "option_c": "Ejecutar codigo JavaScript desde C#",
        "option_d": "Crear web workers",
        "correct": "A",
        "explanation": "CascadingValue/CascadingParameter proporcionan un mecanismo de inyeccion de dependencias para el arbol de componentes, utiles para temas, configuracion o autenticacion compartida."
    },

    # =====================================================================
    # TEMA 28 - Blazor: Componentes avanzados, gestion de estilos
    # =====================================================================
    {
        "topic_num": 28,
        "question": "En Blazor, el ciclo de vida de un componente incluye metodos como OnInitialized, OnParametersSet y:",
        "option_a": "OnClick",
        "option_b": "OnAfterRender",
        "option_c": "OnSubmit",
        "option_d": "OnLoad",
        "correct": "B",
        "explanation": "OnAfterRender (y OnAfterRenderAsync) se invoca despues de que el componente ha renderizado en el DOM. Es util para operaciones que requieren acceso al DOM via JavaScript interop."
    },
    {
        "topic_num": 28,
        "question": "Para aislar CSS a un unico componente Blazor, se utiliza:",
        "option_a": "Un archivo style.css global",
        "option_b": "Un archivo .razor.css con el mismo nombre que el componente (CSS isolation)",
        "option_c": "La directiva @style en el componente",
        "option_d": "Un archivo SCSS compilado manualmente",
        "correct": "B",
        "explanation": "Blazor soporta CSS isolation: un archivo Component.razor.css se emite con un atributo de ambito unico, aplicando los estilos solo a ese componente. El framework lo gestiona automaticamente en tiempo de compilacion."
    },

    # =====================================================================
    # TEMA 29 - Blazor: Formularios y validacion
    # =====================================================================
    {
        "topic_num": 29,
        "question": "En Blazor, el componente `EditForm` se utiliza para:",
        "option_a": "Editar archivos de configuracion del servidor",
        "option_b": "Gestionar formularios de entrada de datos con soporte para validacion de modelo",
        "option_c": "Crear tablas de datos editables",
        "option_d": "Modificar el DOM directamente",
        "correct": "B",
        "explanation": "EditForm es el componente de formularios de Blazor. Se vincula a un modelo via Model='...' y soporta validacion mediante Data Annotations y componentes como DataAnnotationsValidator."
    },
    {
        "topic_num": 29,
        "question": "Para mostrar los mensajes de validacion de un campo especifico en Blazor, se utiliza el componente:",
        "option_a": "ValidationMessage<T>",
        "option_b": "ErrorList",
        "option_c": "FormFeedback",
        "option_d": "FieldError",
        "correct": "A",
        "explanation": "ValidationMessage<TValue> renderiza los mensajes de error asociados a una expresion de campo (For='@(() => model.Property)'). Se combina con DataAnnotationsValidator para mostrar errores de Data Annotations."
    },

    # =====================================================================
    # TEMA 30 - Blazor: Inyeccion de dependencias y servicios
    # =====================================================================
    {
        "topic_num": 30,
        "question": "En Blazor, para solicitar un servicio registrado en el contenedor de DI dentro de un componente, se utiliza el atributo:",
        "option_a": "@using",
        "option_b": "@inject",
        "option_c": "@service",
        "option_d": "@import",
        "correct": "B",
        "explanation": "@inject Tipo Nombre inyecta un servicio desde el contenedor de dependencias (IServiceProvider) en el componente. Se registra services.AddSingleton/Scoped/Transient en Program.cs."
    },
    {
        "topic_num": 30,
        "question": "En ASP.NET Core/Blazor, el ciclo de vida Scoped de un servicio significa que:",
        "option_a": "Se crea una unica instancia para toda la aplicacion",
        "option_b": "Se crea una instancia nueva por cada peticion HTTP (en server) o cada sesion de componente (en WASM con HttpClient)",
        "option_c": "Se crea en cada constructor que lo solicite",
        "option_d": "Se destruye inmediatamente despues de usarlo",
        "correct": "B",
        "explanation": "Scoped crea una instancia por ambito. En Blazor Server coincide con el circuito. En Web APIs ASP.NET Core coincide con la peticion HTTP. No debe usarse para estado compartido entre usuarios (eso es Singleton)."
    },

    # =====================================================================
    # TEMA 31 - Blazor: Gestion de estado
    # =====================================================================
    {
        "topic_num": 31,
        "question": "En Blazor WebAssembly, una forma comun de gestionar estado global compartido entre componentes es:",
        "option_a": "Usar variables estaticas en todos los componentes",
        "option_b": "Crear un servicio inyectado como Singleton que almacene el estado centralizado",
        "option_c": "Guardar todo en localStorage y leerlo en cada renderizado",
        "option_d": "Usar ViewState como en Web Forms",
        "correct": "B",
        "explanation": "Un servicio Singleton (ej. AppState o CartState) inyectado en @inject permite compartir estado entre componentes sin pasar parametros manualmente. Los eventos o StateHasChanged() notifican cambios."
    },
    {
        "topic_num": 31,
        "question": "En Blazor, para notificar a un componente que debe re-renderizarse tras un cambio de estado, se invoca:",
        "option_a": "Render()",
        "option_b": "StateHasChanged()",
        "option_c": "Update()",
        "option_d": "Refresh()",
        "correct": "B",
        "explanation": "StateHasChanged() marca el componente como requiriendo renderizado. El framework lo procesara en el siguiente ciclo de renderizado. Es util en escenarios async o eventos externos."
    },

    # =====================================================================
    # TEMA 32 - Blazor: Navegacion y enrutado
    # =====================================================================
    {
        "topic_num": 32,
        "question": "En Blazor, el componente `NavLink` se diferencia de una etiqueta `a` HTML estandar en que:",
        "option_a": "NavLink solo funciona en Blazor Server",
        "option_b": "NavLink detecta automaticamente la ruta activa y aplica clases CSS de activo",
        "option_c": "NavLink abre enlaces en una nueva pestana siempre",
        "option_d": "NavLink requiere autenticacion obligatoria",
        "correct": "B",
        "explanation": "NavLink renderiza un enlace y anade la clase 'active' (configurable) cuando la URL actual coincide con el href del enlace, mejorando la navegacion con indicadores visuales."
    },
    {
        "topic_num": 32,
        "question": "En Blazor, para navegar programaticamente a otra ruta desde codigo C#, se utiliza:",
        "option_a": "window.location.href",
        "option_b": "NavigationManager con el metodo NavigateTo()",
        "option_c": "Router.Navigate()",
        "option_d": "HttpClient.Get()",
        "correct": "B",
        "explanation": "NavigationManager es un servicio inyectado que proporciona metodos como NavigateTo(string uri) para navegacion programatica, y propiedades como Uri y BaseUri."
    },

    # =====================================================================
    # TEMA 33 - Git: Instalacion, configuracion, trabajo local
    # =====================================================================
    {
        "topic_num": 33,
        "question": "En Git, que comando se utiliza para configurar el nombre de usuario de forma global?",
        "option_a": "git config user.name \"Nombre\"",
        "option_b": "git config --global user.name \"Nombre\"",
        "option_c": "git set user \"Nombre\"",
        "option_d": "git user --set \"Nombre\"",
        "correct": "B",
        "explanation": "git config --global user.name establece el nombre de usuario a nivel global (archivo ~/.gitconfig). Sin --global se aplica solo al repositorio actual."
    },
    {
        "topic_num": 33,
        "question": "En Git, despues de modificar archivos, para prepararlos para el siguiente commit se utiliza:",
        "option_a": "git commit directamente",
        "option_b": "git add <archivo> o git add .",
        "option_c": "git push",
        "option_d": "git stage --all sin comando previo",
        "correct": "B",
        "explanation": "git add mueve los cambios al staging area (indice). Solo los cambios en staging se incluyen en el siguiente commit. git add . anade todos los cambios del directorio actual."
    },

    # =====================================================================
    # TEMA 34 - Git: Ramas, rebase, merge vs rebase, stash
    # =====================================================================
    {
        "topic_num": 34,
        "question": "La diferencia principal entre `git merge` y `git rebase` al integrar cambios de una rama es que:",
        "option_a": "Ambos hacen exactamente lo mismo",
        "option_b": "Merge crea un commit de fusion conservando la historia; rebase reescribe los commits propios sobre la punta de la otra rama, creando una historia lineal",
        "option_c": "Rebase elimina todos los commits de la rama origen",
        "option_d": "Merge solo funciona con ramas locales",
        "correct": "B",
        "explanation": "Merge conserva la historia bifurcada con un commit de merge. Rebase mueve los commits de la rama actual al final de la rama destino, reescribiendo hashes pero generando historial lineal."
    },
    {
        "topic_num": 34,
        "question": "En Git, `git stash` se utiliza para:",
        "option_a": "Eliminar permanentemente cambios no confirmados",
        "option_b": "Guardar temporalmente cambios no confirmados en una pila para recuperarlos despues",
        "option_c": "Fusionar dos ramas rapidamente",
        "option_d": "Publicar cambios en el repositorio remoto",
        "correct": "B",
        "explanation": "git stash guarda el estado del working directory e index en una pila (stash stack), limpiando el working directory. Se recupera con git stash pop o git stash apply."
    },

    # =====================================================================
    # TEMA 35 - Git: Trabajo remoto, flujos de trabajo
    # =====================================================================
    {
        "topic_num": 35,
        "question": "En Git, el flujo de trabajo GitFlow define principalmente las ramas:",
        "option_a": "Solo main y develop",
        "option_b": "main/master, develop, feature/*, release/*, hotfix/* y support/*",
        "option_c": "Solo ramas de integracion continua",
        "option_d": "Una rama unica compartida por todo el equipo",
        "correct": "B",
        "explanation": "GitFlow (Vincent Driessen) define: main (produccion), develop (integracion), feature/* (nuevas funcionalidades), release/* (preparacion de version), hotfix/* (correcciones urgentes en produccion)."
    },
    {
        "topic_num": 35,
        "question": "El comando `git fetch` se diferencia de `git pull` en que:",
        "option_a": "Son exactamente iguales",
        "option_b": "fetch descarga cambios del remoto sin fusionarlos; pull hace fetch + merge automaticamente",
        "option_c": "fetch solo funciona con HTTPS",
        "option_d": "pull solo descarga metadatos sin codigo",
        "correct": "B",
        "explanation": "git fetch actualiza las referencias remotas (origin/main) sin modificar la rama local. git pull = git fetch + git merge, lo que actualiza directamente la rama actual."
    },

    # =====================================================================
    # TEMA 36 - SedipuAlb@: Definiciones y conceptos basicos
    # =====================================================================
    {
        "topic_num": 36,
        "question": "La plataforma SedipuAlb@ es la sede electronica de:",
        "option_a": "La Junta de Comunidades de Castilla-La Mancha",
        "option_b": "La Diputacion Provincial de Albacete",
        "option_c": "El Ayuntamiento de Albacete",
        "option_d": "La Delegacion del Gobierno en Albacete",
        "correct": "B",
        "explanation": "SedipuAlb@ es la plataforma de Administracion Electronica de la Diputacion Provincial de Albacete, que agrupa sus servicios de sede electronica y tramitacion."
    },
    {
        "topic_num": 36,
        "question": "Segun la Ley 39/2015, una sede electronica es:",
        "option_a": "Una pagina web informativa sobre la Administracion",
        "option_b": "El punto de acceso electronico a traves del cual una Administracion Publica comunica a los interesados los actos y actuaciones disponibles via telematica",
        "option_c": "Un centro fisico de atencion al ciudadano",
        "option_d": "Un servidor FTP de descarga de documentos",
        "correct": "B",
        "explanation": "El art. 2.h) LPACAP define sede electronica como el punto de acceso electronico a traves del cual los interesados acceden a la informacion, servicios y tramites de la Administracion."
    },

    # =====================================================================
    # TEMA 37 - SedipuAlb@: Modulos para tramitadores
    # =====================================================================
    {
        "topic_num": 37,
        "question": "El modulo SEFACE de SedipuAlb@ se utiliza para:",
        "option_a": "La gestion del registro electronico",
        "option_b": "La firma electronica y el sellado de tiempo",
        "option_c": "La facturacion electronica",
        "option_d": "La gestion de expedientes",
        "correct": "B",
        "explanation": "SEFACE (Servicio de Firma y Certificacion Electronica) gestiona la firma electronica, sellado de tiempo y validacion de firmas dentro de la plataforma SedipuAlb@."
    },
    {
        "topic_num": 37,
        "question": "El modulo SEGEX de SedipuAlb@ esta relacionado con:",
        "option_a": "La generacion de informes estadisticos",
        "option_b": "La gestion de la sede electronica y publicacion de informacion institucional",
        "option_c": "La interoperabilidad con otras administraciones",
        "option_d": "La gestion de recursos humanos",
        "correct": "B",
        "explanation": "SEGEX (Sede Electronica y Gestion de Expedientes Externos) gestiona la publicacion de informacion en la sede electronica y la atencion a tramites iniciados por ciudadanos."
    },

    # =====================================================================
    # TEMA 38 - Interoperabilidad estatal. SCSP. SARA
    # =====================================================================
    {
        "topic_num": 38,
        "question": "La Red SARA (Sistema de Aplicaciones y Redes para las Administraciones) es:",
        "option_a": "Una red social para funcionarios publicos",
        "option_b": "La red de comunicaciones de las Administraciones Publicas espanolas que garantiza la interoperabilidad y seguridad",
        "option_c": "Un buscador universal de tramites administrativos",
        "option_d": "Un protocolo de transferencia de archivos FTP seguro",
        "correct": "B",
        "explanation": "La Red SARA es la red corporativa de comunicaciones del sector publico estatal, gestionada por el Ministerio de Asuntos Economicos y Transformacion Digital, que conecta las AAPP para el intercambio seguro de informacion."
    },
    {
        "topic_num": 38,
        "question": "El Protocolo SCSP (Sistema de Comunicaciones Seguras entre las Administraciones Publicas) permite:",
        "option_a": "Solo el envio de correos electronicos cifrados",
        "option_b": "El intercambio de datos y la verificacion de identidades entre administraciones de forma estandarizada y segura",
        "option_c": "La videoconferencia entre oficinas de registro",
        "option_d": "La impresion remota de documentos administrativos",
        "correct": "B",
        "explanation": "SCSP define especificaciones para el intercambio seguro de datos entre AAPP, incluyendo protocolos de verificacion de datos de identidad, residencia, etc., sobre la Red SARA."
    },

    # =====================================================================
    # TEMA 39 - Servicios compartidos
    # =====================================================================
    {
        "topic_num": 39,
        "question": "Cl@ve es un sistema del Gobierno de Espana que proporciona:",
        "option_a": "Un almacenamiento en nube para documentos administrativos",
        "option_b": "Identificacion y autenticacion electronica de ciudadanos mediante distintos niveles de seguridad (Cl@ve Permanente, Cl@ve PIN, certificado)",
        "option_c": "Un buscador de empleo publico",
        "option_d": "Una plataforma de firma masiva de contratos publicos",
        "correct": "B",
        "explanation": "Cl@ve es el sistema electronico de identificacion y firma del Gobierno de Espana. Nivel basico con usuario/contrasena + SMS (Cl@ve PIN), nivel avanzado con certificado o DNIe (Cl@ve Permanente)."
    },
    {
        "topic_num": 39,
        "question": "La Carpeta Ciudadana del ciudadano permite principalmente:",
        "option_a": "Guardar documentos personales en la nube privada",
        "option_b": "Consultar notificaciones, comunicaciones, expedientes y actuaciones administrativas en las distintas administraciones publicas",
        "option_c": "Solicitar prestamos publicos",
        "option_d": "Gestionar la nomina de empleados publicos",
        "correct": "B",
        "explanation": "La Carpeta Ciudadana (carpeta Ciudadana del Punto de Acceso General) es un espacio personal donde los ciudadanos pueden consultar sus tramites, notificaciones y relaciones con todas las AAPP."
    },

    # =====================================================================
    # TEMA 40 - Accesibilidad Web
    # =====================================================================
    {
        "topic_num": 40,
        "question": "El nivel de conformidad AA de las WCAG 2.1 requiere:",
        "option_a": "Solo los criterios de nivel A",
        "option_b": "Todos los criterios de nivel A mas criterios adicionales de nivel AA",
        "option_c": "Solo criterios de nivel AAA",
        "option_d": "Ningun criterio especifico, solo recomendaciones",
        "correct": "B",
        "explanation": "WCAG define tres niveles: A (minimo), AA (nivel medio, requerido por la normativa europea), AAA (maximo). AA incluye todos los criterios A mas criterios adicionales como contraste de color mejorado."
    },
    {
        "topic_num": 40,
        "question": "Segun la Directiva (UE) 2016/2102 y la norma UNE-EN 301549, las paginas web de las Administraciones Publicas deben ser:",
        "option_a": "Accesibles solo desde navegadores Microsoft Edge",
        "option_b": "Accesibles para personas con discapacidad, cumpliendo niveles de conformidad WCAG 2.1 AA",
        "option_c": "Desarrolladas unicamente en HTML4",
        "option_d": "Sin contenido multimedia para facilitar la navegacion",
        "correct": "B",
        "explanation": "La Directiva 2016/2102 exige que los sitios web y apps moviles de las AAPP sean accesibles, conformes con la norma UNE-EN 301549 (que incorpora WCAG 2.1 nivel AA) y publiquen declaraciones de accesibilidad."
    },
]


# =====================================================================
# EXTRA QUESTIONS GENERATED FROM temario.md
# =====================================================================
# The first 80 questions above are detailed questions. The following block
# expands the bank with additional mobile-study questions for every tema.
# They are intentionally static/deterministic so the GitHub Pages app can
# work without a backend.

_TOPIC_STUDY_POINTS = {
    1: ["estructura de la Constitucion", "Titulo Preliminar", "derechos y deberes fundamentales", "Cortes Generales"],
    2: ["Gobierno y Administracion", "relaciones Gobierno-Cortes", "organizacion territorial", "comunidades autonomas"],
    3: ["organizacion municipal", "alcalde y pleno", "organizacion provincial", "diputacion provincial"],
    4: ["texto refundido de regimen local", "ROF", "organizacion de entidades locales", "funcionamiento local"],
    5: ["interesados en el procedimiento", "capacidad de obrar", "representacion", "registros administrativos"],
    6: ["actividad administrativa", "requisitos del acto administrativo", "eficacia de los actos", "nulidad y anulabilidad"],
    7: ["prevencion de riesgos laborales", "principios de accion preventiva", "derecho a proteccion eficaz", "obligaciones de trabajadores"],
    8: ["igualdad efectiva", "discriminacion por razon de sexo", "igualdad en el trabajo", "violencia de genero en Castilla-La Mancha"],
    9: ["firma electronica", "certificado digital", "AutoFirma", "validacion de firma"],
    10: ["cifrado simetrico y asimetrico", "PKI", "SSL/TLS", "PGP"],
    11: ["Esquema Nacional de Seguridad", "politica de seguridad", "medidas de seguridad", "categorias de sistemas"],
    12: ["proteccion de datos personales", "RGPD", "principios del tratamiento", "derechos de las personas interesadas"],
    13: ["arquitectura servidor PostgreSQL", "procesos de servidor", "cluster de bases de datos", "conexion cliente-servidor"],
    14: ["jerarquia de objetos PostgreSQL", "esquemas", "funciones", "roles y permisos"],
    15: ["transacciones PostgreSQL", "ACID", "COMMIT y ROLLBACK", "aislamiento"],
    16: ["psql", "pg_dump", "pg_restore", "importacion y exportacion de datos"],
    17: ["optimizacion SQL", "indices", "EXPLAIN", "configuracion de servidor PostgreSQL"],
    18: ["fundamentos de C#", "tipos y variables", "clases y objetos", "control de flujo"],
    19: ["patron MVC", "controladores y vistas", "Bootstrap", "sitios web ASP.NET Core"],
    20: ["Entity Framework Core", "DbContext", "entidades", "migraciones"],
    21: ["LINQ", "consultas sobre colecciones", "expresiones lambda", "proyecciones y filtros"],
    22: ["model binding", "validacion", "modificacion de datos con EF", "tareas asincronas"],
    23: ["autenticacion", "autorizacion", "claims y roles", "filtros ASP.NET Core"],
    24: ["Web API", "servicios REST", "controladores API", "codigos HTTP"],
    25: ["OData", "exposicion de datos", "consultas con $filter", "consultas con $select"],
    26: ["Blazor", "modelos de alojamiento", "Blazor Server", "Blazor WebAssembly"],
    27: ["componentes Blazor", "binding", "parametros", "valores en cascada"],
    28: ["componentes avanzados", "gestion de estilos", "CSS isolation", "RenderFragment"],
    29: ["formularios Blazor", "EditForm", "DataAnnotations", "validacion"],
    30: ["inyeccion de dependencias", "configuracion de servicios", "contenedor DI", "ciclos de vida de servicios"],
    31: ["gestion de estado", "estado de componente", "estado compartido", "persistencia de estado"],
    32: ["navegacion Blazor", "enrutado", "NavigationManager", "parametros de ruta"],
    33: ["teoria de Git", "configuracion de Git", "repositorio local", "commit"],
    34: ["ramas en Git", "merge", "rebase", "stash"],
    35: ["repositorios remotos", "push y pull", "pull request", "estrategias de ramas"],
    36: ["SedipuAlba", "sede electronica", "registro electronico", "expediente electronico"],
    37: ["Segex", "Sefycu", "Segra", "Seres y Secoin"],
    38: ["interoperabilidad estatal", "SCSP", "Red SARA", "intercambio de datos entre administraciones"],
    39: ["Cl@ve", "DNIe", "FIRe", "Carpeta Ciudadana"],
    40: ["accesibilidad web", "WCAG", "UNE-EN 301549", "nivel AA"],
}

_EXTRA_DISTRACTORS = [
    "edicion de video digital", "maquetacion editorial impresa", "administracion de nominas privadas",
    "diseño de hardware electronico", "marketing en redes sociales", "gestion de almacenes fisicos",
    "produccion audiovisual", "calculo de estructuras de obra civil", "contabilidad financiera avanzada",
]


def _make_extra_questions():
    questions = []
    all_points = [point for points in _TOPIC_STUDY_POINTS.values() for point in points]
    for topic_num, points in _TOPIC_STUDY_POINTS.items():
        for idx, point in enumerate(points, start=1):
            # Mix distractors from unrelated study points and generic concepts.
            other_points = [p for p in all_points if p not in points]
            distractors = [
                other_points[(topic_num * 7 + idx * 3) % len(other_points)],
                other_points[(topic_num * 11 + idx * 5) % len(other_points)],
                _EXTRA_DISTRACTORS[(topic_num + idx) % len(_EXTRA_DISTRACTORS)],
            ]
            options = [point] + distractors
            # Rotate the correct answer so it is not always A.
            shift = (topic_num + idx) % 4
            options = options[shift:] + options[:shift]
            correct = "ABCD"[options.index(point)]
            questions.append({
                "topic_num": topic_num,
                "question": f"Tema {topic_num}: cual de los siguientes contenidos es clave para estudiar este tema?",
                "option_a": options[0].capitalize(),
                "option_b": options[1].capitalize(),
                "option_c": options[2].capitalize(),
                "option_d": options[3].capitalize(),
                "correct": correct,
                "explanation": f"'{point}' forma parte del nucleo del Tema {topic_num} segun el temario oficial.",
            })
    return questions


SEED_QUESTIONS.extend(_make_extra_questions())
