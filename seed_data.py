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
# EXTRA QUESTIONS CURATED FROM temario.md
# =====================================================================
# The first 80 questions above are detailed questions. This block adds
# shorter mobile-study questions, but avoids generic prompts such as
# "que contenido es clave". Each question asks for a concrete concept,
# tool, law, principle, protocol, command, framework feature, or module.

_EXTRA_EXACT_SPECS = {
    1: [
        ("Que parte de la Constitucion Espanola de 1978 recoge los valores superiores del ordenamiento juridico?", "Titulo Preliminar", ["Titulo IV", "Titulo VIII", "Disposicion derogatoria"], "El Titulo Preliminar recoge, entre otros aspectos, los valores superiores, la soberania nacional y la forma politica del Estado."),
        ("Que institucion ejerce la potestad legislativa del Estado segun la Constitucion?", "Cortes Generales", ["Consejo de Estado", "Tribunal Constitucional", "Defensor del Pueblo"], "Las Cortes Generales representan al pueblo espanol y ejercen la potestad legislativa del Estado."),
    ],
    2: [
        ("Que titulo constitucional regula el Gobierno y la Administracion?", "Titulo IV", ["Titulo I", "Titulo III", "Titulo X"], "El Titulo IV de la Constitucion regula el Gobierno y la Administracion."),
        ("Que titulo constitucional trata la organizacion territorial del Estado?", "Titulo VIII", ["Titulo II", "Titulo V", "Titulo IX"], "El Titulo VIII regula municipios, provincias y comunidades autonomas."),
    ],
    3: [
        ("Segun la Ley 7/1985, que entidad local basica tiene personalidad juridica y plena capacidad para el cumplimiento de sus fines?", "Municipio", ["Comarca", "Mancomunidad", "Area metropolitana"], "El municipio es la entidad local basica de la organizacion territorial del Estado."),
        ("En la organizacion municipal comun, que organo preside la corporacion?", "Alcalde", ["Interventor", "Secretario", "Tesorero"], "El alcalde preside la corporacion municipal y dirige el gobierno y la administracion municipal."),
    ],
    4: [
        ("Que norma aprueba el texto refundido de las disposiciones legales vigentes en materia de regimen local?", "Real Decreto Legislativo 781/1986", ["Ley Organica 3/2018", "Real Decreto 203/2021", "Ley 40/2015"], "El Real Decreto Legislativo 781/1986 aprueba el texto refundido de regimen local."),
        ("Que reglamento regula la organizacion, funcionamiento y regimen juridico de las entidades locales?", "ROF", ["ENS", "RGPD", "TREBEP"], "El ROF es el Reglamento de Organizacion, Funcionamiento y Regimen Juridico de las Entidades Locales."),
    ],
    5: [
        ("En la Ley 39/2015, como se denomina quien promueve un procedimiento administrativo como titular de derechos o intereses legitimos?", "Interesado", ["Contratista", "Fedatario", "Encargado del tratamiento"], "La Ley 39/2015 define quienes tienen la condicion de interesados en el procedimiento administrativo."),
        ("Que permite acreditar que una persona actua en nombre de otra ante la Administracion?", "Representacion", ["Recusacion", "Convalidacion", "Publicacion"], "La representacion permite actuar ante las Administraciones Publicas por medio de otra persona."),
    ],
    6: [
        ("Que vicio afecta a un acto administrativo que lesiona derechos fundamentales?", "Nulidad de pleno derecho", ["Anulabilidad leve", "Caducidad", "Prescripcion"], "Los actos que lesionan derechos y libertades susceptibles de amparo constitucional son nulos de pleno derecho."),
        ("Que requisito exige que el acto administrativo exponga las razones juridicas y facticas de su decision?", "Motivacion", ["Notificacion por edictos", "Archivo", "Desistimiento"], "La motivacion explica los hechos y fundamentos de derecho que justifican el acto."),
    ],
    7: [
        ("En prevencion de riesgos laborales, que principio exige combatir los riesgos en su origen?", "Principio de accion preventiva", ["Principio de caja unica", "Principio de publicidad registral", "Principio de devengo"], "La accion preventiva incluye evitar riesgos, evaluarlos y combatirlos en su origen."),
        ("Que derecho tiene el trabajador frente a los riesgos laborales?", "Proteccion eficaz en seguridad y salud", ["Libre eleccion de proveedor", "Secreto profesional absoluto", "Exencion de formacion"], "La Ley 31/1995 reconoce el derecho a una proteccion eficaz en materia de seguridad y salud en el trabajo."),
    ],
    8: [
        ("Que ley estatal regula la igualdad efectiva de mujeres y hombres?", "Ley Organica 3/2007", ["Ley 7/1985", "Ley 31/1995", "Ley 9/2017"], "La Ley Organica 3/2007 regula la igualdad efectiva de mujeres y hombres."),
        ("Que tipo de discriminacion se produce cuando una medida aparentemente neutra perjudica especialmente a personas de un sexo?", "Discriminacion indirecta", ["Discriminacion positiva prohibida", "Recusacion", "Silencio administrativo"], "La discriminacion indirecta deriva de disposiciones, criterios o practicas aparentemente neutros con efecto desfavorable."),
    ],
    9: [
        ("Que aplicacion se utiliza habitualmente en la Administracion espanola para firmar electronicamente desde el navegador o escritorio?", "AutoFirma", ["pg_restore", "Bootstrap", "Git stash"], "AutoFirma permite realizar firmas electronicas con certificados digitales en equipos de usuario."),
        ("Que elemento vincula unos datos de verificacion de firma a un firmante y confirma su identidad?", "Certificado digital", ["Indice SQL", "Controlador MVC", "RenderFragment"], "El certificado digital asocia la identidad del titular con sus claves criptograficas."),
    ],
    10: [
        ("Que infraestructura gestiona certificados digitales, autoridades de certificacion y revocacion?", "PKI", ["LINQ", "SCSP", "OData"], "Una PKI organiza certificados, autoridades de certificacion, registro y mecanismos de revocacion."),
        ("Que protocolo protege comunicaciones web mediante cifrado sobre HTTP?", "TLS", ["PGP", "SIR", "MVC"], "HTTPS utiliza TLS para autenticar el servidor y cifrar la comunicacion."),
    ],
    11: [
        ("Que norma establece la politica de seguridad para la utilizacion de medios electronicos en el sector publico espanol?", "Esquema Nacional de Seguridad", ["Bootstrap", "Entity Framework Core", "WCAG"], "El ENS fija principios, requisitos y medidas de seguridad para sistemas del sector publico."),
        ("En el ENS, que determina la intensidad de las medidas de seguridad aplicables a un sistema?", "Categoria del sistema", ["Color corporativo", "Numero de usuarios anonimos", "Tipo de navegador"], "La categoria del sistema condiciona las medidas de seguridad que deben aplicarse."),
    ],
    12: [
        ("Que reglamento europeo regula la proteccion de datos personales y su libre circulacion?", "RGPD", ["ROF", "ENS", "PGP"], "El Reglamento (UE) 2016/679 es el Reglamento General de Proteccion de Datos."),
        ("Que principio exige tratar solo los datos personales adecuados, pertinentes y limitados a lo necesario?", "Minimizacion de datos", ["Devengo", "Rebase", "Polimorfismo"], "La minimizacion limita los datos tratados a los necesarios para la finalidad perseguida."),
    ],
    13: [
        ("En PostgreSQL, como se denomina el conjunto de bases de datos gestionadas por una misma instancia?", "Cluster de bases de datos", ["Pull request", "Valor en cascada", "Sede electronica"], "Un cluster PostgreSQL es el conjunto de bases de datos de una instancia del servidor."),
        ("Que proceso de PostgreSQL acepta conexiones de clientes y crea procesos de servidor?", "Postmaster", ["Kestrel", "AutoFirma", "NavigationManager"], "El proceso principal de PostgreSQL escucha conexiones y coordina procesos del servidor."),
    ],
    14: [
        ("En PostgreSQL, que objeto agrupa tablas, vistas y funciones dentro de una base de datos?", "Esquema", ["Commit", "Claim", "Componente Razor"], "Los esquemas organizan objetos dentro de una base de datos PostgreSQL."),
        ("Que mecanismo de PostgreSQL permite controlar privilegios de usuarios y grupos?", "Roles", ["Filtros MVC", "WCAG", "Ramas"], "PostgreSQL usa roles para usuarios, grupos y asignacion de permisos."),
    ],
    15: [
        ("Que instruccion confirma definitivamente una transaccion en PostgreSQL?", "COMMIT", ["ROLLBACK", "EXPLAIN", "STASH"], "COMMIT confirma los cambios realizados en una transaccion."),
        ("Que propiedad ACID garantiza que una transaccion se ejecuta completa o no se aplica?", "Atomicidad", ["Cascada", "Enrutado", "Accesibilidad"], "La atomicidad evita estados parciales: la transaccion se completa entera o se deshace."),
    ],
    16: [
        ("Que herramienta de PostgreSQL genera copias de seguridad logicas de una base de datos?", "pg_dump", ["psql", "pg_restore", "AutoFirma"], "pg_dump exporta una base de datos PostgreSQL en formatos logicos de copia."),
        ("Que comando de PostgreSQL se usa para restaurar copias en formato personalizado o directorio?", "pg_restore", ["pg_dump", "git rebase", "dotnet run"], "pg_restore restaura copias creadas por pg_dump en formatos no planos."),
    ],
    17: [
        ("Que sentencia de PostgreSQL muestra el plan de ejecucion de una consulta?", "EXPLAIN", ["COMMIT", "SELECT DISTINCT", "MERGE"], "EXPLAIN permite analizar como PostgreSQL ejecutara una consulta."),
        ("Que estructura acelera busquedas a cambio de espacio y coste de mantenimiento?", "Indice", ["RenderFragment", "Certificado", "Sede"], "Los indices mejoran consultas, aunque ocupan espacio y afectan a escrituras."),
    ],
    18: [
        ("En C#, que palabra clave declara una clase?", "class", ["SELECT", "branch", "route"], "La palabra clave class declara tipos de referencia definidos por el usuario."),
        ("En C#, que instruccion permite iterar sobre una coleccion elemento a elemento?", "foreach", ["rollback", "rebase", "scaffold"], "foreach recorre los elementos de una coleccion o secuencia enumerable."),
    ],
    19: [
        ("En MVC, que componente recibe la peticion y selecciona la respuesta adecuada?", "Controlador", ["Vista", "Migracion", "Certificado"], "El controlador procesa la entrada, coordina el modelo y devuelve una vista o resultado."),
        ("Que framework CSS se cita en el temario para construir sitios web responsive?", "Bootstrap", ["PostgreSQL", "AutoFirma", "Cl@ve"], "Bootstrap proporciona componentes y rejilla responsive para interfaces web."),
    ],
    20: [
        ("En Entity Framework Core, que clase representa la sesion con la base de datos y permite consultar entidades?", "DbContext", ["Controller", "EditForm", "Postmaster"], "DbContext coordina consultas, seguimiento de cambios y persistencia en EF Core."),
        ("En EF Core, que mecanismo aplica cambios del modelo al esquema de la base de datos?", "Migraciones", ["Claims", "Stash", "Valores en cascada"], "Las migraciones versionan y aplican cambios de esquema derivados del modelo."),
    ],
    21: [
        ("Que tecnologia de .NET permite consultar colecciones con sintaxis integrada en el lenguaje?", "LINQ", ["SCSP", "PKI", "WCAG"], "LINQ integra consultas sobre colecciones, objetos y proveedores de datos."),
        ("En LINQ, que tipo de expresion se usa frecuentemente para definir predicados y proyecciones?", "Expresion lambda", ["Certificado X.509", "Nivel AA", "Sede electronica"], "Las lambdas permiten expresar funciones anonimas usadas en Where, Select y otros operadores."),
    ],
    22: [
        ("En ASP.NET Core MVC, que proceso enlaza valores de la peticion HTTP con parametros o propiedades del modelo?", "Model binding", ["Rebase", "Cifrado simetrico", "Revocacion"], "El model binding asigna datos de rutas, formularios o query string al modelo de accion."),
        ("Que palabra clave de C# permite esperar una tarea asincrona sin bloquear el hilo?", "await", ["commit", "select", "grant"], "await espera la finalizacion de una Task dentro de metodos asincronos."),
    ],
    23: [
        ("Que proceso verifica la identidad de un usuario?", "Autenticacion", ["Autorizacion", "Indexacion", "Enrutado"], "La autenticacion responde a quien es el usuario."),
        ("Que proceso decide si un usuario autenticado puede acceder a un recurso?", "Autorizacion", ["Autenticacion", "Serializacion", "Compilacion"], "La autorizacion determina permisos sobre acciones o recursos."),
    ],
    24: [
        ("Que estilo de servicio web suele exponer recursos mediante verbos HTTP como GET, POST, PUT y DELETE?", "REST", ["PGP", "ROF", "Stash"], "Las API REST usan recursos identificados por URI y operaciones HTTP."),
        ("En HTTP, que codigo indica que una peticion se ha completado correctamente?", "200 OK", ["404 Not Found", "500 Internal Server Error", "301 Moved Permanently"], "200 OK indica respuesta satisfactoria para la peticion."),
    ],
    25: [
        ("Que estandar permite consultar datos expuestos mediante parametros como $filter y $select?", "OData", ["SCSP", "TLS", "FIRe"], "OData define convenciones para exponer y consultar datos mediante HTTP."),
        ("En OData, que parametro selecciona solo determinadas propiedades de una entidad?", "$select", ["$filter", "$orderby", "$top"], "$select limita las propiedades devueltas por el servicio."),
    ],
    26: [
        ("Que modelo de alojamiento de Blazor ejecuta componentes en el servidor y actualiza la interfaz mediante SignalR?", "Blazor Server", ["Blazor WebAssembly", "MVC clasico", "Web API"], "Blazor Server mantiene la logica en el servidor y sincroniza la UI con SignalR."),
        ("Que modelo de Blazor ejecuta la aplicacion .NET en el navegador del cliente?", "Blazor WebAssembly", ["Blazor Server", "Razor Pages", "Windows Forms"], "Blazor WebAssembly ejecuta codigo .NET en el navegador mediante WebAssembly."),
    ],
    27: [
        ("En Blazor, que directiva se usa habitualmente para enlazar un valor de la interfaz con una propiedad?", "@bind", ["@route", "@inject", "@page"], "@bind implementa enlace de datos entre controles y propiedades."),
        ("En Blazor, que atributo marca una propiedad para recibir valores desde un componente padre?", "[Parameter]", ["[Key]", "[Authorize]", "[Required]"], "[Parameter] permite pasar datos de un componente padre a uno hijo."),
    ],
    28: [
        ("En Blazor, que tipo permite pasar fragmentos de interfaz como contenido reutilizable?", "RenderFragment", ["DbContext", "Claim", "Postmaster"], "RenderFragment representa un fragmento de UI renderizable."),
        ("Que tecnica de Blazor limita estilos CSS al componente correspondiente?", "CSS isolation", ["TLS", "LINQ", "OData"], "CSS isolation genera estilos con ambito para evitar efectos globales no deseados."),
    ],
    29: [
        ("Que componente de Blazor encapsula un formulario con validacion integrada?", "EditForm", ["DbSet", "Controller", "Router"], "EditForm coordina modelo, envio y validacion en formularios Blazor."),
        ("Que atributos de .NET se usan habitualmente para reglas de validacion como Required o StringLength?", "DataAnnotations", ["Claims", "Migrations", "RenderFragments"], "DataAnnotations permite declarar reglas de validacion sobre modelos."),
    ],
    30: [
        ("Que patron permite solicitar servicios en constructores o componentes sin crearlos manualmente?", "Inyeccion de dependencias", ["Cifrado simetrico", "Consulta OData", "Rebase interactivo"], "La inyeccion de dependencias desacopla clases de la creacion de sus dependencias."),
        ("En .NET, que ciclo de vida crea una instancia nueva del servicio en cada solicitud HTTP?", "Scoped", ["Singleton", "Transient", "Static"], "Scoped mantiene una instancia por ambito, normalmente por solicitud web."),
    ],
    31: [
        ("En Blazor, como se denomina la informacion mantenida por un componente durante su renderizado e interaccion?", "Estado de componente", ["Indice SQL", "Certificado digital", "Categoria ENS"], "El estado de componente incluye valores que afectan a su interfaz y comportamiento."),
        ("Que tecnica permite conservar datos de usuario aunque se recargue la pagina en el navegador?", "Persistencia de estado", ["Rollback", "Revocacion", "Normalizacion"], "La persistencia de estado puede usar almacenamiento local, sesion u otros mecanismos."),
    ],
    32: [
        ("En Blazor, que directiva define la ruta URL de un componente pagina?", "@page", ["@bind", "@code", "@typeparam"], "@page declara la plantilla de ruta que activa el componente como pagina."),
        ("Que servicio de Blazor permite navegar por codigo y obtener la URI actual?", "NavigationManager", ["DbContext", "Postmaster", "AutoFirma"], "NavigationManager proporciona metodos y propiedades para navegacion y URI."),
    ],
    33: [
        ("Que comando inicializa un repositorio Git local?", "git init", ["git push", "git merge", "git clone --bare"], "git init crea la estructura inicial del repositorio local."),
        ("Que comando registra una instantanea de los cambios preparados en Git?", "git commit", ["git stash", "git fetch", "git reset --hard"], "git commit guarda en el historial los cambios del area de preparacion."),
    ],
    34: [
        ("Que operacion de Git reaplica commits sobre otra base de historial?", "rebase", ["merge", "stash", "tag"], "Rebase mueve o reaplica commits encima de otra referencia base."),
        ("Que comando guarda temporalmente cambios no confirmados para limpiar el arbol de trabajo?", "git stash", ["git branch", "git blame", "git remote"], "git stash aparta cambios locales para recuperarlos posteriormente."),
    ],
    35: [
        ("Que comando envia commits locales a un repositorio remoto?", "git push", ["git pull", "git fetch", "git status"], "git push publica commits locales en el remoto configurado."),
        ("Que practica propone integrar cambios mediante revision antes de fusionarlos en la rama principal?", "Pull request", ["Rollback", "Certificado digital", "Model binding"], "Una pull request facilita revision, debate y validaciones antes de integrar cambios."),
    ],
    36: [
        ("En administracion electronica, que punto permite a la ciudadania acceder electronicamente a servicios y tramites?", "Sede electronica", ["Indice B-tree", "RenderFragment", "Repositorio bare"], "La sede electronica es la direccion electronica disponible para relaciones con la Administracion."),
        ("Que concepto agrupa documentos, actuaciones y metadatos de un procedimiento administrativo electronico?", "Expediente electronico", ["Cluster PostgreSQL", "Pull request", "Claim"], "El expediente electronico reune documentos y actuaciones del procedimiento."),
    ],
    37: [
        ("En SedipuAlba, que modulo se asocia a la gestion de expedientes?", "Segex", ["Sefycu", "Segra", "Secoin"], "Segex es el modulo de gestion de expedientes de la plataforma."),
        ("En SedipuAlba, que modulo se asocia a la firma y custodia de documentos?", "Sefycu", ["Segex", "Segra", "Seres"], "Sefycu se relaciona con firma y custodia documental dentro de la plataforma."),
    ],
    38: [
        ("Que red conecta administraciones publicas espanolas para intercambio seguro de informacion?", "Red SARA", ["Red TOR", "Red CDN", "Red NAT privada"], "La Red SARA facilita comunicaciones seguras entre Administraciones Publicas."),
        ("Que especificaciones permiten consultar datos de otras administraciones evitando pedir documentos al ciudadano?", "SCSP", ["OData", "PGP", "WCAG"], "SCSP estandariza servicios de verificacion y consulta de datos entre administraciones."),
    ],
    39: [
        ("Que sistema comun permite identificacion, autenticacion y firma para ciudadanos ante las AAPP?", "Cl@ve", ["Bootstrap", "pg_dump", "LINQ"], "Cl@ve es una plataforma comun de identificacion y autenticacion del sector publico."),
        ("Que servicio facilita la firma electronica centralizada en el sector publico?", "FIRe", ["SIR", "PID", "WCAG"], "FIRe facilita integracion de servicios de firma electronica en aplicaciones publicas."),
    ],
    40: [
        ("Que pautas internacionales sirven de referencia para accesibilidad del contenido web?", "WCAG", ["ACID", "PKI", "LINQ"], "Las WCAG establecen criterios de accesibilidad para contenido web."),
        ("Que nivel de conformidad WCAG es el exigido habitualmente por la normativa europea para el sector publico?", "AA", ["A", "AAA", "Beta"], "La normativa suele tomar como referencia WCAG nivel AA."),
    ],
}


def _make_extra_questions():
    questions = []
    for topic_num, specs in _EXTRA_EXACT_SPECS.items():
        for idx, (question, answer, distractors, explanation) in enumerate(specs, start=1):
            options = [answer] + list(distractors)
            # Rotate the correct answer so it is not always A.
            shift = (topic_num + idx) % 4
            options = options[shift:] + options[:shift]
            correct = "ABCD"[options.index(answer)]
            questions.append({
                "topic_num": topic_num,
                "question": question,
                "option_a": options[0],
                "option_b": options[1],
                "option_c": options[2],
                "option_d": options[3],
                "correct": correct,
                "explanation": explanation,
            })
    return questions


SEED_QUESTIONS.extend(_make_extra_questions())


# =====================================================================
# DIRECT QUESTION FILLER TO REACH ABOUT 30 QUESTIONS PER TOPIC
# =====================================================================
# These questions are intentionally NOT "which topic does X belong to".
# They ask direct exam-style questions about commands, concepts, definitions,
# tools, protocols, principles or practical use cases.

_TOPIC_SHORT_TITLES = {
    1: "Constitucion Espanola de 1978",
    2: "Gobierno, Administracion y organizacion territorial",
    3: "Ley 7/1985 y regimen local basico",
    4: "RDL 781/1986 y ROF",
    5: "Ley 39/2015: interesados, registros y plazos",
    6: "Ley 39/2015: actos y procedimiento administrativo",
    7: "Prevencion de riesgos laborales",
    8: "Igualdad",
    9: "Firma electronica",
    10: "Criptografia y certificados",
    11: "Esquema Nacional de Seguridad",
    12: "Proteccion de datos",
    13: "PostgreSQL servidor",
    14: "PostgreSQL objetos y permisos",
    15: "PostgreSQL transacciones",
    16: "PostgreSQL herramientas cliente",
    17: "PostgreSQL optimizacion",
    18: "C#",
    19: "MVC y Bootstrap",
    20: "Entity Framework Core",
    21: "LINQ",
    22: "Model binding, validacion y asincronia",
    23: "Autenticacion y autorizacion",
    24: "Web API",
    25: "OData",
    26: "Blazor alojamiento",
    27: "Blazor componentes",
    28: "Blazor avanzado y estilos",
    29: "Blazor formularios",
    30: "Blazor servicios",
    31: "Blazor estado",
    32: "Blazor navegacion",
    33: "Git local",
    34: "Git ramas",
    35: "Git remoto",
    36: "SedipuAlba conceptos",
    37: "SedipuAlba modulos",
    38: "Interoperabilidad estatal",
    39: "Servicios compartidos AAPP",
    40: "Accesibilidad web",
}

_DIRECT_POOLS = {
    1: [
        ("Que parte de la Constitucion proclama valores como libertad, justicia, igualdad y pluralismo politico?", "Titulo Preliminar", ["Titulo IV", "Titulo VIII", "Titulo X"], "El art. 1 CE, dentro del Titulo Preliminar, proclama esos valores superiores."),
        ("Que articulo de la Constitucion reconoce el derecho a la vida y a la integridad fisica y moral?", "Articulo 15", ["Articulo 1", "Articulo 27", "Articulo 137"], "El articulo 15 CE reconoce el derecho a la vida y a la integridad fisica y moral."),
        ("Que camaras forman las Cortes Generales?", "Congreso de los Diputados y Senado", ["Gobierno y Senado", "Tribunal Supremo y Congreso", "Consejo de Estado y Senado"], "Las Cortes Generales son bicamerales: Congreso y Senado."),
        ("Que forma politica del Estado espanol establece la Constitucion?", "Monarquia parlamentaria", ["Republica federal", "Monarquia absoluta", "Confederacion autonoma"], "El art. 1.3 CE establece la monarquia parlamentaria."),
        ("Donde reside la soberania nacional segun la Constitucion?", "En el pueblo espanol", ["En las Cortes exclusivamente", "En el Gobierno", "En las comunidades autonomas"], "El art. 1.2 CE indica que la soberania nacional reside en el pueblo espanol."),
        ("Que institucion representa al pueblo espanol y ejerce la potestad legislativa del Estado?", "Cortes Generales", ["Consejo de Ministros", "Tribunal Constitucional", "Defensor del Pueblo"], "Las Cortes Generales representan al pueblo y ejercen la potestad legislativa."),
    ],
    2: [
        ("Que organo dirige la politica interior y exterior, la Administracion civil y militar y la defensa del Estado?", "Gobierno", ["Senado", "Consejo General del Poder Judicial", "Tribunal de Cuentas"], "La Constitucion atribuye esas funciones al Gobierno."),
        ("Quien propone al Rey el nombramiento y separacion de los ministros?", "Presidente del Gobierno", ["Presidente del Congreso", "Defensor del Pueblo", "Presidente del Senado"], "Corresponde al Presidente del Gobierno proponer el nombramiento y separacion de ministros."),
        ("Que mecanismo parlamentario permite exigir responsabilidad politica al Gobierno mediante candidato alternativo?", "Mocion de censura", ["Recurso de amparo", "Cuestion prejudicial", "Iniciativa legislativa popular"], "La mocion de censura espanola es constructiva y exige candidato alternativo."),
        ("Que entidades integran la organizacion territorial basica del Estado?", "Municipios, provincias y comunidades autonomas", ["Ministerios, juzgados y diputaciones", "Comarcas, partidos judiciales y distritos", "Cabildos, islas y parroquias exclusivamente"], "La Constitucion reconoce municipios, provincias y comunidades autonomas."),
        ("Que principio constitucional reconoce autonomia para la gestion de intereses propios?", "Autonomia", ["Jerarquia normativa", "Irretroactividad penal", "Unidad jurisdiccional"], "La CE reconoce autonomia a municipios, provincias y comunidades autonomas."),
        ("Que camara puede retirar la confianza al Gobierno mediante mocion de censura?", "Congreso de los Diputados", ["Senado", "Tribunal Constitucional", "Consejo de Estado"], "La responsabilidad politica del Gobierno se exige ante el Congreso."),
    ],
    3: [
        ("Que entidad local basica tiene personalidad juridica y plena capacidad para cumplir sus fines?", "Municipio", ["Barrio", "Distrito censal", "Partido judicial"], "La LRBRL define el municipio como entidad local basica."),
        ("Que registro administrativo acredita la residencia y domicilio de los vecinos de un municipio?", "Padron municipal", ["Registro Civil", "Inventario de bienes", "Libro de actas"], "El padron municipal contiene los vecinos del municipio."),
        ("Que organo municipal esta integrado por todos los concejales y presidido por el alcalde?", "Pleno", ["Junta electoral", "Intervencion", "Tesoreria"], "El Pleno lo forman los concejales y lo preside el alcalde."),
        ("Que organo unipersonal dirige el gobierno y la administracion municipal?", "Alcalde", ["Secretario", "Interventor", "Tesorero"], "El alcalde dirige el gobierno y la administracion municipal."),
        ("Que entidad local agrupa municipios y tiene como fines la asistencia y cooperacion municipal?", "Provincia", ["Mancomunidad privada", "Comunidad de bienes", "Distrito hipotecario"], "La provincia garantiza solidaridad y asistencia a municipios."),
        ("Que institucion gobierna y administra la provincia?", "Diputacion provincial", ["Subdelegacion del Gobierno", "Audiencia Provincial", "Delegacion de Hacienda"], "El gobierno y administracion autonoma de la provincia corresponde a la Diputacion u organos equivalentes."),
    ],
    4: [
        ("Que norma aprueba el texto refundido de disposiciones legales vigentes en materia de regimen local?", "Real Decreto Legislativo 781/1986", ["Ley 39/2015", "Ley Organica 3/2018", "Real Decreto 203/2021"], "El RDL 781/1986 aprueba el texto refundido de regimen local."),
        ("Que significan las siglas ROF en regimen local?", "Reglamento de Organizacion, Funcionamiento y Regimen Juridico", ["Registro Oficial de Funcionarios", "Reglamento Organico Fiscal", "Relacion Ordinaria de Funciones"], "El ROF regula organizacion, funcionamiento y regimen juridico de entidades locales."),
        ("Que documento recoge formalmente lo tratado y acordado en una sesion de organo colegiado local?", "Acta", ["Padron", "Edicto tributario", "Orden de pago"], "El acta documenta asistentes, deliberaciones esenciales y acuerdos."),
        ("Que tipo de norma local puede aprobar una entidad local dentro de sus competencias?", "Ordenanza", ["Ley organica", "Real decreto legislativo", "Tratado internacional"], "Las entidades locales pueden aprobar ordenanzas y reglamentos en su ambito competencial."),
        ("Que requisito formal permite convocar validamente una sesion de un organo colegiado local?", "Convocatoria", ["Empadronamiento", "Recurso de casacion", "Certificado digital cualificado"], "La convocatoria comunica sesion, fecha, hora y asuntos a tratar."),
        ("Que expresion identifica el conjunto de reglas aplicables a organizacion y funcionamiento de entidades locales?", "Regimen juridico local", ["Regimen hipotecario", "Regimen sancionador penal", "Regimen electoral europeo"], "El regimen juridico local ordena competencias, organos, funcionamiento y actos locales."),
    ],
    5: [
        ("Como se denomina la persona que promueve un procedimiento administrativo por ser titular de derechos o intereses legitimos?", "Interesado", ["Fedatario", "Licitador", "Administrador concursal"], "La Ley 39/2015 regula la condicion de interesado."),
        ("Que figura permite actuar ante la Administracion en nombre de otra persona?", "Representacion", ["Recusacion", "Abstencion", "Convalidacion"], "La representacion acredita que una persona actua por otra."),
        ("Que sistema permite presentar solicitudes, escritos y comunicaciones ante la Administracion?", "Registro administrativo", ["Padron electoral", "Inventario contable", "Registro mercantil privado"], "Los registros administrativos reciben y anotan documentos dirigidos a la Administracion."),
        ("Como se computan normalmente los plazos expresados en dias en la Ley 39/2015 si no se indica otra cosa?", "Dias habiles", ["Dias naturales", "Solo sabados", "Solo dias lectivos"], "Si la norma no dice otra cosa, los plazos por dias son habiles."),
        ("Que medio permite registrar documentos por via telematica?", "Registro electronico", ["Libro de caja", "Indice B-tree", "Repositorio Git"], "El registro electronico permite la presentacion electronica de documentos."),
        ("Que capacidad permite comparecer y actuar validamente ante las Administraciones Publicas?", "Capacidad de obrar", ["Capacidad contributiva exclusivamente", "Capacidad procesal penal", "Capacidad de endeudamiento"], "La Ley 39/2015 regula quienes tienen capacidad de obrar ante las AAPP."),
    ],
    6: [
        ("Que requisito explica los hechos y fundamentos de derecho de un acto administrativo?", "Motivacion", ["Caducidad", "Prescripcion", "Reformatio in peius"], "La motivacion justifica la decision administrativa."),
        ("Que comunicacion formal pone un acto administrativo en conocimiento de la persona interesada?", "Notificacion", ["Compulsa", "Alegacion", "Avocacion"], "La notificacion comunica el acto al interesado."),
        ("Que vicio se produce en actos que lesionan derechos fundamentales?", "Nulidad de pleno derecho", ["Anulabilidad leve", "Subsanacion automatica", "Silencio estimatorio obligatorio"], "La lesion de derechos fundamentales determina nulidad de pleno derecho."),
        ("Que fase del procedimiento incluye pruebas, informes y audiencia?", "Instruccion", ["Terminacion", "Archivo definitivo inicial", "Ejecucion presupuestaria"], "La instruccion realiza los actos necesarios para determinar y comprobar datos."),
        ("Que forma normal pone fin a un procedimiento administrativo resolviendo el fondo?", "Resolucion", ["Providencia bancaria", "Asiento contable", "Diligencia penal"], "La resolucion decide las cuestiones planteadas en el procedimiento."),
        ("Que defecto permite impugnar un acto pero no lo hace nulo de pleno derecho?", "Anulabilidad", ["Inexistencia fisica", "Derogacion constitucional", "Cosa juzgada penal"], "La anulabilidad cubre infracciones no incluidas en nulidad de pleno derecho."),
    ],
    7: [
        ("Que norma basica regula la prevencion de riesgos laborales en Espana?", "Ley 31/1995", ["Ley 7/1985", "Ley 39/2015", "Ley 9/2017"], "La Ley 31/1995 es la norma basica de prevencion de riesgos laborales."),
        ("Que principio preventivo exige eliminar el riesgo antes que proteger frente a el?", "Evitar los riesgos", ["Transferir siempre el riesgo", "Asegurar solo economicamente", "Ignorar riesgos leves"], "La accion preventiva empieza por evitar los riesgos."),
        ("Que actuacion identifica y valora peligros para la seguridad y salud de los trabajadores?", "Evaluacion de riesgos", ["Liquidacion tributaria", "Auditoria contable", "Recurso de alzada"], "La evaluacion de riesgos permite planificar la actividad preventiva."),
        ("Que derecho tiene el trabajador en materia de seguridad y salud laboral?", "Proteccion eficaz", ["Renuncia preventiva", "Secreto salarial absoluto", "Libre incumplimiento de instrucciones"], "El trabajador tiene derecho a proteccion eficaz frente a riesgos laborales."),
        ("Que debe hacer el trabajador con los equipos de proteccion proporcionados?", "Usarlos correctamente", ["Venderlos", "Ignorarlos", "Modificar siempre su diseno"], "Los trabajadores deben usar adecuadamente medios y equipos de proteccion."),
        ("Que concepto describe la posibilidad de que un trabajador sufra un dano derivado del trabajo?", "Riesgo laboral", ["Padron laboral", "Credito horario", "Turno voluntario"], "Riesgo laboral es la posibilidad de dano derivado del trabajo."),
    ],
    8: [
        ("Que ley estatal regula la igualdad efectiva de mujeres y hombres?", "Ley Organica 3/2007", ["Ley 31/1995", "Ley 7/1985", "Ley 40/2015"], "La LO 3/2007 regula la igualdad efectiva."),
        ("Que trato desfavorable por razon de sexo se produce de forma expresa y visible?", "Discriminacion directa", ["Discriminacion indirecta", "Recusacion", "Prescripcion"], "La discriminacion directa supone trato menos favorable por razon de sexo."),
        ("Que discriminacion deriva de una medida aparentemente neutra con impacto desfavorable?", "Discriminacion indirecta", ["Abstencion", "Convalidacion", "Silencio administrativo"], "La discriminacion indirecta puede surgir de criterios aparentemente neutros."),
        ("Que instrumento empresarial ordena medidas para alcanzar igualdad de trato y oportunidades?", "Plan de igualdad", ["Plan de tesoreria", "Plan de urbanismo", "Plan de backup"], "Los planes de igualdad ordenan objetivos y medidas de igualdad."),
        ("Que conducta verbal, no verbal o fisica de naturaleza sexual atenta contra la dignidad?", "Acoso sexual", ["Acoso urbanistico", "Fraude de ley", "Enriquecimiento injusto"], "El acoso sexual es una conducta de naturaleza sexual que crea entorno intimidatorio u ofensivo."),
        ("Que principio exige ausencia de discriminacion por sexo en empleo, formacion y promocion?", "Igualdad de trato", ["Jerarquia contable", "Unidad de caja", "Devengo"], "La igualdad de trato impide discriminacion directa o indirecta por sexo."),
    ],
    9: [
        ("Que permite acreditar la identidad del firmante en una firma electronica?", "Certificado digital", ["Indice SQL", "Controlador MVC", "Hoja de estilos"], "El certificado digital vincula identidad y claves criptograficas."),
        ("Que clave debe mantenerse secreta por el titular para firmar electronicamente?", "Clave privada", ["Clave publica", "Certificado raiz", "Hash publicado"], "La clave privada se protege y se usa para crear la firma."),
        ("Que aplicacion se usa habitualmente para firmar documentos electronicamente en AAPP espanolas?", "AutoFirma", ["pg_dump", "Bootstrap", "Git stash"], "AutoFirma permite firmar con certificados digitales."),
        ("Que proceso comprueba que una firma electronica es valida y no ha sido alterada?", "Validacion de firma", ["Normalizacion SQL", "Renderizado CSS", "Rebase interactivo"], "Validar firma comprueba integridad, certificado y estado."),
        ("Que servicio acredita el momento en que existia una firma o documento?", "Sellado de tiempo", ["Compilacion JIT", "Indexacion B-tree", "Model binding"], "El sellado de tiempo aporta evidencia temporal."),
        ("Que tipo de firma electronica tiene maximas garantias juridicas con certificado cualificado y dispositivo cualificado?", "Firma cualificada", ["Firma simple manuscrita escaneada", "Firma anonima", "Firma por usuario invitado"], "La firma electronica cualificada tiene los requisitos reforzados del Reglamento eIDAS."),
    ],
    10: [
        ("Que cifrado utiliza la misma clave para cifrar y descifrar?", "Cifrado simetrico", ["Cifrado asimetrico", "Hash sin clave", "Firma digital"], "El cifrado simetrico comparte una clave secreta."),
        ("Que cifrado utiliza un par de claves publica y privada?", "Cifrado asimetrico", ["Cifrado simetrico", "Compresion ZIP", "Codificacion Base64"], "El cifrado asimetrico usa clave publica y privada."),
        ("Que infraestructura gestiona certificados, autoridades de certificacion y revocacion?", "PKI", ["LINQ", "OData", "MVC"], "La PKI organiza certificados y autoridades de certificacion."),
        ("Que entidad emite y firma certificados digitales?", "Autoridad de certificacion", ["Router web", "Controlador API", "Repositorio Git"], "La CA emite certificados y garantiza su vinculacion."),
        ("Que protocolo cifra comunicaciones web usadas por HTTPS?", "TLS", ["PGP", "FTP", "SMTP sin cifrar"], "HTTPS funciona sobre TLS para cifrar la comunicacion."),
        ("Que tecnologia se asocia historicamente al cifrado y firma de correo o ficheros mediante pares de claves?", "PGP", ["WCAG", "SCSP", "SIR"], "PGP permite cifrar y firmar informacion con criptografia de clave publica."),
    ],
    11: [
        ("Que esquema fija principios y requisitos de seguridad para sistemas del sector publico?", "ENS", ["OData", "Bootstrap", "LINQ"], "El Esquema Nacional de Seguridad establece la politica de seguridad en medios electronicos."),
        ("Que documento define objetivos, organizacion y responsabilidades de seguridad?", "Politica de seguridad", ["Plan de marketing", "Hoja de calculo", "Contrato menor"], "La politica de seguridad ordena criterios y responsabilidades."),
        ("Que actividad identifica amenazas, vulnerabilidades e impacto sobre la informacion?", "Analisis de riesgos", ["Rebase", "Model binding", "Empadronamiento"], "El analisis de riesgos permite seleccionar medidas adecuadas."),
        ("Que determina si un sistema ENS es de categoria basica, media o alta?", "Categoria del sistema", ["Color de la interfaz", "Numero de pantallas", "Lenguaje de programacion"], "La categoria se obtiene valorando dimensiones de seguridad."),
        ("Que revisa periodicamente el cumplimiento de medidas de seguridad?", "Auditoria", ["Compilacion", "Minificacion", "Paginacion"], "La auditoria comprueba el cumplimiento del ENS."),
        ("Que conjunto de controles se aplica para proteger informacion y servicios?", "Medidas de seguridad", ["Estilos CSS", "Ramas Git", "Consultas LINQ"], "Las medidas protegen confidencialidad, integridad, disponibilidad, autenticidad y trazabilidad."),
    ],
    12: [
        ("Que reglamento europeo regula la proteccion de datos personales?", "RGPD", ["ROF", "ENS", "PGP"], "El Reglamento UE 2016/679 es el RGPD."),
        ("Como se llama la persona fisica identificada o identificable sobre la que trata la informacion?", "Interesado", ["Encargado", "Delegado", "Autoridad de certificacion"], "El interesado es la persona cuyos datos se tratan."),
        ("Quien decide los fines y medios del tratamiento de datos personales?", "Responsable del tratamiento", ["Encargado del tratamiento", "Usuario anonimo", "Proveedor DNS"], "El responsable determina fines y medios del tratamiento."),
        ("Quien trata datos personales por cuenta del responsable?", "Encargado del tratamiento", ["Responsable", "Afectado", "Autoridad judicial siempre"], "El encargado trata datos siguiendo instrucciones del responsable."),
        ("Que principio exige tratar solo datos adecuados, pertinentes y necesarios?", "Minimizacion de datos", ["Maximizacion documental", "Rebase", "Indexacion"], "La minimizacion limita los datos a lo necesario."),
        ("Que derecho permite obtener confirmacion de si se tratan datos personales propios?", "Derecho de acceso", ["Derecho de tanteo", "Derecho de superficie", "Derecho de retracto"], "El derecho de acceso permite conocer el tratamiento de datos propios."),
    ],
    13: [
        ("Que SGBD objeto-relacional de codigo abierto se estudia en el temario?", "PostgreSQL", ["Photoshop", "AutoFirma", "Bootstrap"], "PostgreSQL es el sistema de bases de datos del bloque."),
        ("Que puerto TCP utiliza PostgreSQL por defecto?", "5432", ["80", "443", "25"], "PostgreSQL escucha por defecto en el puerto 5432."),
        ("Como se llama el conjunto de bases de datos gestionadas por una instancia PostgreSQL?", "Cluster", ["Pull request", "RenderFragment", "Sede electronica"], "Un cluster PostgreSQL agrupa bases de datos de una instancia."),
        ("Que proceso principal acepta conexiones y coordina procesos en PostgreSQL?", "Postmaster", ["NavigationManager", "AutoFirma", "Kestrel siempre"], "El proceso principal de PostgreSQL gestiona conexiones."),
        ("Que registro garantiza durabilidad y recuperacion ante fallos en PostgreSQL?", "WAL", ["CSS", "JWT", "CSV"], "Write-Ahead Logging registra cambios antes de aplicarlos definitivamente."),
        ("Que memoria compartida cachea paginas de datos en PostgreSQL?", "shared buffers", ["localStorage", "sessionStorage", "RenderTree"], "shared_buffers define memoria para cache de paginas de datos."),
    ],
    14: [
        ("Que objeto PostgreSQL agrupa tablas, vistas y funciones dentro de una base de datos?", "Schema", ["Commit", "Claim", "Cookie"], "Los schemas organizan objetos dentro de una base de datos."),
        ("Que objeto almacena filas y columnas de datos?", "Table", ["Sequence", "Role", "Index only"], "Las tablas almacenan datos en filas y columnas."),
        ("Que objeto representa una consulta almacenada que se usa como tabla virtual?", "View", ["Role", "Trigger solamente", "Backup"], "Una vista encapsula una consulta."),
        ("Que objeto genera valores numericos consecutivos habitualmente usados como claves?", "Sequence", ["Schema", "Grant", "Policy"], "Las secuencias generan numeros consecutivos."),
        ("Que sentencia concede privilegios en PostgreSQL?", "GRANT", ["ROLLBACK", "EXPLAIN", "VACUUM"], "GRANT concede permisos sobre objetos."),
        ("Que entidad PostgreSQL puede representar usuarios o grupos y recibir permisos?", "Role", ["View", "Table", "Sequence"], "Los roles gestionan usuarios, grupos y privilegios."),
    ],
    15: [
        ("Que instruccion inicia una transaccion explicita en PostgreSQL?", "BEGIN", ["EXPLAIN", "VACUUM", "GRANT"], "BEGIN abre una transaccion."),
        ("Que instruccion confirma los cambios de una transaccion?", "COMMIT", ["ROLLBACK", "SAVEPOINT", "SELECT"], "COMMIT hace permanentes los cambios."),
        ("Que instruccion deshace los cambios de una transaccion?", "ROLLBACK", ["COMMIT", "GRANT", "ANALYZE"], "ROLLBACK cancela la transaccion."),
        ("Que propiedad ACID evita resultados parciales de una transaccion?", "Atomicidad", ["Durabilidad", "Aislamiento", "Indexacion"], "La atomicidad implica todo o nada."),
        ("Que propiedad ACID garantiza que los cambios confirmados sobreviven a fallos?", "Durabilidad", ["Atomicidad", "Consistencia visual", "Polimorfismo"], "La durabilidad conserva cambios confirmados."),
        ("Que tecnica de PostgreSQL permite concurrencia manteniendo multiples versiones de filas?", "MVCC", ["MVC", "WCAG", "PKI"], "MVCC significa Multi-Version Concurrency Control."),
    ],
    16: [
        ("Que cliente de linea de comandos permite ejecutar SQL contra PostgreSQL?", "psql", ["pg_dump", "pg_restore", "AutoFirma"], "psql es el cliente interactivo de PostgreSQL."),
        ("Que herramienta crea copias logicas de seguridad de bases PostgreSQL?", "pg_dump", ["psql", "VACUUM", "git push"], "pg_dump exporta una base de datos."),
        ("Que herramienta restaura copias en formato personalizado o directorio?", "pg_restore", ["pg_dump", "COPY", "EXPLAIN"], "pg_restore restaura backups creados con pg_dump en ciertos formatos."),
        ("Que instruccion importa o exporta datos entre tablas y ficheros?", "COPY", ["GRANT", "BEGIN", "REBASE"], "COPY transfiere datos entre tablas y archivos."),
        ("Que formato de texto separado por comas se usa a menudo para importar y exportar datos?", "CSV", ["JWT", "CSS", "PDF firmado"], "CSV es habitual para intercambio tabular."),
        ("Que herramienta grafica se usa frecuentemente para administrar PostgreSQL?", "pgAdmin", ["AutoFirma", "Visual Studio Code exclusivamente", "Cl@ve"], "pgAdmin es una herramienta grafica de administracion PostgreSQL."),
    ],
    17: [
        ("Que sentencia muestra el plan de ejecucion estimado de una consulta?", "EXPLAIN", ["COMMIT", "GRANT", "COPY"], "EXPLAIN muestra el plan de ejecucion."),
        ("Que variante ejecuta realmente la consulta y muestra tiempos reales?", "EXPLAIN ANALYZE", ["EXPLAIN ONLY", "ROLLBACK ANALYZE", "GRANT ANALYZE"], "EXPLAIN ANALYZE ejecuta y mide."),
        ("Que estructura acelera busquedas a cambio de espacio y coste de escritura?", "Indice", ["Vista sin materializar siempre", "Rol", "Schema"], "Los indices mejoran lecturas concretas."),
        ("Que tipo de indice es el mas habitual para igualdad y rangos en PostgreSQL?", "B-tree", ["JWT", "WCAG", "CSV"], "B-tree es el tipo por defecto y mas comun."),
        ("Que operacion recopila estadisticas para el planificador?", "ANALYZE", ["COMMIT", "SAVEPOINT", "GRANT"], "ANALYZE actualiza estadisticas."),
        ("Que operacion limpia tuplas muertas y ayuda a controlar el bloat?", "VACUUM", ["ROLLBACK", "FETCH", "PUSH"], "VACUUM recupera espacio reutilizable y mantiene la salud de tablas."),
    ],
    18: [
        ("Que palabra clave declara una clase en C#?", "class", ["select", "branch", "route"], "class declara una clase."),
        ("Que bloque captura excepciones en C#?", "catch", ["foreach", "namespace", "return"], "catch captura excepciones lanzadas en un try."),
        ("Que palabra clave permite implementar una interfaz en una clase?", ":", ["implements", "extends", "using as always"], "En C# se usa dos puntos para herencia e implementacion."),
        ("Que instruccion recorre una coleccion elemento a elemento?", "foreach", ["switch", "throw", "lock"], "foreach itera sobre colecciones enumerables."),
        ("Que mecanismo permite definir tipos reutilizables con parametros de tipo?", "Genericos", ["Namespaces", "Comentarios XML", "Directivas using"], "Los genericos permiten clases y metodos parametrizados por tipo."),
        ("Que miembro expone datos de una clase mediante get y set?", "Propiedad", ["Namespace", "Assembly", "Paquete NuGet"], "Las propiedades encapsulan acceso a datos."),
    ],
    19: [
        ("En MVC, que componente recibe la peticion y coordina la respuesta?", "Controlador", ["Vista", "Modelo", "Migracion"], "El controlador procesa la entrada y devuelve resultados."),
        ("En MVC, que componente representa datos y reglas de negocio?", "Modelo", ["Vista", "Controlador", "Layout"], "El modelo contiene datos y logica de dominio."),
        ("En MVC, que componente genera la interfaz presentada al usuario?", "Vista", ["Modelo", "Controlador", "Repositorio remoto"], "La vista renderiza la salida."),
        ("Que motor de plantillas se usa habitualmente en ASP.NET Core MVC?", "Razor", ["Jinja", "Twig", "Blade exclusivamente"], "Razor combina HTML y C#."),
        ("Que framework CSS proporciona rejilla responsive y componentes?", "Bootstrap", ["PostgreSQL", "AutoFirma", "Git"], "Bootstrap facilita interfaces responsive."),
        ("Que archivo o plantilla suele definir estructura comun de varias vistas?", "Layout", ["DbContext", "Controller", "Migration"], "El layout comparte cabecera, menu y estructura."),
    ],
    20: [
        ("Que clase representa la sesion de trabajo con la base de datos en EF Core?", "DbContext", ["DbSet", "Controller", "EditForm"], "DbContext coordina consultas y persistencia."),
        ("Que propiedad representa una coleccion consultable de entidades?", "DbSet", ["DbContext", "Migration", "Claim"], "DbSet representa entidades de un tipo."),
        ("Que metodo guarda en base de datos los cambios pendientes?", "SaveChanges", ["AddScoped", "NavigateTo", "Authorize"], "SaveChanges persiste cambios rastreados."),
        ("Que mecanismo versiona cambios del modelo al esquema de base de datos?", "Migraciones", ["Claims", "Stash", "RenderFragments"], "Las migraciones aplican cambios de esquema."),
        ("Que enfoque parte de clases C# para generar o actualizar la base de datos?", "Code First", ["Database Last", "View Only", "Static First"], "Code First define el modelo en codigo."),
        ("Que caracteristica recuerda cambios en entidades cargadas para persistirlos?", "Change tracking", ["Model binding", "Routing", "Hashing"], "El seguimiento de cambios detecta modificaciones de entidades."),
    ],
    21: [
        ("Que operador LINQ filtra elementos por una condicion?", "Where", ["Select", "OrderBy", "Join"], "Where aplica un predicado."),
        ("Que operador LINQ transforma cada elemento en otra forma?", "Select", ["Where", "GroupBy", "Skip"], "Select realiza proyecciones."),
        ("Que operador LINQ ordena ascendentemente una secuencia?", "OrderBy", ["Join", "Where", "Take"], "OrderBy ordena por una clave."),
        ("Que operador LINQ agrupa elementos por clave?", "GroupBy", ["Select", "Where", "Any"], "GroupBy crea grupos segun una clave."),
        ("Que interfaz permite construir consultas que un proveedor puede traducir, por ejemplo a SQL?", "IQueryable", ["IEnumerable", "IDisposable", "IComparable"], "IQueryable representa consultas traducibles por proveedores."),
        ("Que expresion anonima se usa mucho en predicados LINQ como x => x.Id > 0?", "Lambda", ["Delegate multicast siempre", "Namespace", "Atributo"], "Las lambdas expresan funciones anonimas."),
    ],
    22: [
        ("Que proceso enlaza datos HTTP con parametros o propiedades del modelo?", "Model binding", ["Routing DNS", "Rebase", "Cifrado"], "Model binding toma datos de ruta, query, formulario o cuerpo."),
        ("Que coleccion indica si el modelo recibido supera las reglas de validacion?", "ModelState", ["DbSet", "ClaimsPrincipal", "HttpClient"], "ModelState almacena estado de validacion."),
        ("Que atributo DataAnnotations exige que un campo tenga valor?", "Required", ["StringLength", "Key", "Table"], "Required marca un campo obligatorio."),
        ("Que palabra clave espera una tarea asincrona?", "await", ["yield", "lock", "base"], "await espera una Task sin bloquear de forma tradicional."),
        ("Que tipo representa una operacion asincrona en .NET?", "Task", ["ThreadStatic", "ActionFilter", "DbSet"], "Task representa trabajo asincrono."),
        ("Que token permite solicitar cancelacion cooperativa de una operacion asincrona?", "CancellationToken", ["AntiForgeryToken", "JwtToken", "RefreshToken siempre"], "CancellationToken comunica cancelacion."),
    ],
    23: [
        ("Que proceso verifica la identidad del usuario?", "Autenticacion", ["Autorizacion", "Serializacion", "Indexacion"], "Autenticacion responde quien es el usuario."),
        ("Que proceso decide si un usuario puede acceder a un recurso?", "Autorizacion", ["Autenticacion", "Compilacion", "Normalizacion"], "Autorizacion responde que puede hacer."),
        ("Que atributo restringe acceso a controladores o acciones en ASP.NET Core?", "Authorize", ["AllowAnonymous", "Required", "HttpGet"], "Authorize exige usuario o politica autorizada."),
        ("Que atributo permite acceso anonimo anulando restricciones de autorizacion?", "AllowAnonymous", ["Authorize", "ValidateAntiForgeryToken", "FromBody"], "AllowAnonymous habilita acceso sin autenticar."),
        ("Que formato de token se usa habitualmente para autenticacion stateless en APIs?", "JWT", ["CSV", "CSS", "WAL"], "JWT transporta claims firmados."),
        ("Que elemento representa afirmaciones sobre un usuario, como nombre o rol?", "Claim", ["Index", "Schema", "View"], "Un claim es una declaracion sobre la identidad."),
    ],
    24: [
        ("Que verbo HTTP se usa normalmente para obtener un recurso?", "GET", ["POST", "PUT", "DELETE"], "GET solicita representaciones de recursos."),
        ("Que verbo HTTP se usa normalmente para crear un recurso?", "POST", ["GET", "DELETE", "OPTIONS"], "POST se usa para crear o enviar datos."),
        ("Que verbo HTTP se usa normalmente para reemplazar o actualizar un recurso?", "PUT", ["GET", "TRACE", "HEAD"], "PUT actualiza o reemplaza un recurso."),
        ("Que verbo HTTP se usa normalmente para eliminar un recurso?", "DELETE", ["GET", "POST", "PATCH only"], "DELETE solicita borrar un recurso."),
        ("Que codigo HTTP indica recurso no encontrado?", "404 Not Found", ["200 OK", "201 Created", "204 No Content"], "404 indica que no se encontro el recurso."),
        ("Que formato ligero se usa habitualmente para intercambiar datos en Web API?", "JSON", ["BMP", "WAV", "EXE"], "JSON es comun en APIs REST."),
    ],
    25: [
        ("Que parametro OData filtra resultados segun una condicion?", "$filter", ["$select", "$top", "$skip"], "$filter limita entidades por condicion."),
        ("Que parametro OData selecciona propiedades concretas?", "$select", ["$filter", "$orderby", "$count"], "$select limita campos devueltos."),
        ("Que parametro OData ordena resultados?", "$orderby", ["$skip", "$top", "$expand always"], "$orderby define ordenacion."),
        ("Que parametro OData limita el numero de resultados devueltos?", "$top", ["$filter", "$select", "$metadata"], "$top establece un maximo."),
        ("Que parametro OData omite un numero de resultados iniciales?", "$skip", ["$top", "$select", "$format"], "$skip se usa para paginacion."),
        ("Que documento describe el modelo de datos expuesto por un servicio OData?", "$metadata", ["$filter", "$top", "$skip"], "$metadata expone metadatos del servicio."),
    ],
    26: [
        ("Que modelo de Blazor ejecuta la logica en servidor y sincroniza la UI con SignalR?", "Blazor Server", ["Blazor WebAssembly", "MVC", "Web API"], "Blazor Server mantiene circuito SignalR con el servidor."),
        ("Que modelo de Blazor ejecuta .NET en el navegador mediante WebAssembly?", "Blazor WebAssembly", ["Blazor Server", "Razor Pages", "Windows Forms"], "Blazor WebAssembly corre en el cliente."),
        ("Que tecnologia permite comunicacion en tiempo real usada por Blazor Server?", "SignalR", ["OData", "PGP", "SCSP"], "SignalR mantiene comunicacion bidireccional."),
        ("Que carpeta contiene activos estaticos publicos en una aplicacion Blazor?", "wwwroot", ["bin", "obj", "Migrations always"], "wwwroot almacena archivos estaticos."),
        ("Que archivo suele configurar servicios y pipeline en una app .NET moderna?", "Program.cs", ["README.md", "package-lock.json", "web.config exclusively"], "Program.cs contiene configuracion de arranque."),
        ("Como se denomina un componente de interfaz reutilizable escrito con Razor?", "Razor component", ["DbContext", "Migration", "Controller only"], "Los componentes Razor son bloques UI de Blazor."),
    ],
    27: [
        ("Que directiva Blazor realiza enlace de datos bidireccional?", "@bind", ["@page", "@inject", "@code"], "@bind sincroniza valor y propiedad."),
        ("Que atributo permite recibir valores desde un componente padre?", "[Parameter]", ["[Key]", "[Required]", "[Authorize]"], "[Parameter] marca parametros de componente."),
        ("Que tipo se usa para notificar eventos desde un componente hijo al padre?", "EventCallback", ["DbSet", "Claim", "CancellationToken"], "EventCallback permite callbacks de eventos."),
        ("Que componente permite suministrar un valor a descendientes sin pasarlo parametro a parametro?", "CascadingValue", ["EditForm", "NavLink", "AuthorizeView only"], "CascadingValue proporciona valores en cascada."),
        ("Que bloque contiene codigo C# dentro de un componente Razor?", "@code", ["@page", "@bind", "@using only"], "@code contiene miembros y logica del componente."),
        ("Que metodo de ciclo de vida se ejecuta al inicializar un componente?", "OnInitialized", ["SaveChanges", "ConfigureServices", "Main"], "OnInitialized se llama durante la inicializacion."),
    ],
    28: [
        ("Que tipo Blazor representa un fragmento de interfaz renderizable?", "RenderFragment", ["DbContext", "Claim", "Postmaster"], "RenderFragment permite contenido reutilizable."),
        ("Que parametro suele contener el contenido hijo no nombrado de un componente?", "ChildContent", ["ModelState", "DbSet", "HttpContext"], "ChildContent recibe contenido anidado."),
        ("Que directiva declara un parametro de tipo generico en un componente?", "@typeparam", ["@bind", "@page", "@inject"], "@typeparam define componentes genericos."),
        ("Que tecnica limita CSS al componente correspondiente?", "CSS isolation", ["TLS", "LINQ", "OData"], "CSS isolation evita colisiones globales."),
        ("Que mecanismo permite componer componentes pasando plantillas de UI?", "Plantillas con RenderFragment", ["ROLLBACK", "GRANT", "pg_dump"], "Las plantillas permiten personalizar renderizado."),
        ("Que archivo suele acompañar a un componente para estilos aislados?", ".razor.css", [".sql", ".dll.config", ".gitignore only"], "Los estilos aislados se colocan en archivos .razor.css."),
    ],
    29: [
        ("Que componente Blazor encapsula formularios con validacion?", "EditForm", ["DbSet", "Controller", "Router"], "EditForm coordina modelo y validacion."),
        ("Que objeto mantiene el estado de edicion y validacion de un formulario?", "EditContext", ["DbContext", "HttpClient", "Claim"], "EditContext sigue cambios y validacion."),
        ("Que componente valida usando atributos DataAnnotations?", "DataAnnotationsValidator", ["ValidationSummary", "InputText", "NavLink"], "DataAnnotationsValidator activa esas reglas."),
        ("Que componente muestra un resumen de errores de validacion?", "ValidationSummary", ["InputSelect", "Router", "AuthorizeView"], "ValidationSummary lista errores."),
        ("Que componente Blazor captura texto en formularios?", "InputText", ["InputNumber", "InputSelect", "EditContext"], "InputText enlaza entradas de texto."),
        ("Que atributo valida longitud maxima o minima de una cadena?", "StringLength", ["Required", "Key", "Table"], "StringLength limita longitud de strings."),
    ],
    30: [
        ("Que patron suministra dependencias sin crearlas manualmente en la clase?", "Inyeccion de dependencias", ["Cifrado simetrico", "Consulta OData", "Rebase"], "DI desacopla creacion y uso de servicios."),
        ("Que registro crea una instancia de servicio por ambito o solicitud?", "AddScoped", ["AddSingleton", "AddTransient", "AddStatic"], "Scoped crea una instancia por scope."),
        ("Que registro reutiliza una unica instancia durante la vida de la aplicacion?", "AddSingleton", ["AddScoped", "AddTransient", "AddPerRequest"], "Singleton comparte una instancia."),
        ("Que registro crea una instancia nueva cada vez que se solicita el servicio?", "AddTransient", ["AddSingleton", "AddScoped", "AddGlobal"], "Transient crea instancias nuevas."),
        ("Que directiva inyecta un servicio en un componente Blazor?", "@inject", ["@bind", "@page", "@typeparam"], "@inject declara dependencias en Razor."),
        ("Que archivo suele contener valores de configuracion JSON de una app .NET?", "appsettings.json", ["package-lock.json", "README.md", "index.html"], "appsettings.json guarda configuracion."),
    ],
    31: [
        ("Que almacenamiento del navegador conserva datos incluso tras cerrar y abrir el navegador?", "localStorage", ["sessionStorage", "RenderFragment", "DbSet"], "localStorage persiste mas alla de la sesion."),
        ("Que almacenamiento del navegador se asocia a la sesion de la pestaña?", "sessionStorage", ["localStorage", "Indexed Route", "DbContext"], "sessionStorage dura la sesion de la pestaña."),
        ("Que patron centraliza datos compartidos entre componentes?", "Servicio de estado", ["Indice B-tree", "Certificado X.509", "Migracion"], "Un servicio de estado comparte datos y notifica cambios."),
        ("Que estado pertenece internamente a un componente concreto?", "Estado de componente", ["Estado global del servidor siempre", "WAL", "JWT"], "El estado de componente afecta a su renderizado."),
        ("Que mecanismo Blazor permite compartir valores descendentes sin parametro directo?", "Cascading state", ["pg_restore", "git fetch", "OData"], "Los valores en cascada pueden transportar estado."),
        ("Que objetivo tiene persistir estado en una aplicacion?", "Conservar datos entre interacciones o recargas", ["Borrar siempre al renderizar", "Impedir navegacion", "Desactivar validacion"], "Persistir estado evita perder informacion util."),
    ],
    32: [
        ("Que directiva define la ruta URL de un componente pagina?", "@page", ["@bind", "@code", "@inject"], "@page declara rutas."),
        ("Que servicio permite navegar por codigo en Blazor?", "NavigationManager", ["DbContext", "Postmaster", "AutoFirma"], "NavigationManager expone NavigateTo y URI."),
        ("Que metodo de NavigationManager cambia la ubicacion actual?", "NavigateTo", ["SaveChanges", "AddScoped", "ROLLBACK"], "NavigateTo navega a una URI."),
        ("Que componente crea enlaces de navegacion con clase activa?", "NavLink", ["EditForm", "InputText", "DbSet"], "NavLink ayuda en menus de navegacion."),
        ("Que componente Blazor selecciona el componente a mostrar segun la ruta?", "Router", ["EditContext", "DbContext", "Controller"], "Router resuelve rutas."),
        ("Que elemento de ruta permite recibir valores desde la URL?", "Parametro de ruta", ["Claim", "Indice", "Certificado"], "Los parametros de ruta capturan segmentos de URL."),
    ],
    33: [
        ("Que comando inicializa un repositorio Git?", "git init", ["git push", "git merge", "git fetch"], "git init crea el repositorio local."),
        ("Que comando muestra el estado del arbol de trabajo?", "git status", ["git commit", "git clone", "git tag"], "git status informa cambios y rama."),
        ("Que comando prepara archivos para el proximo commit?", "git add", ["git push", "git pull", "git reset --hard always"], "git add lleva cambios al staging area."),
        ("Que comando crea una instantanea en el historial?", "git commit", ["git fetch", "git remote", "git stash"], "git commit registra cambios preparados."),
        ("Que archivo indica patrones que Git debe ignorar?", ".gitignore", ["README.md", "package.json", "pyproject.toml"], ".gitignore contiene reglas de exclusion."),
        ("Que puntero representa normalmente el commit actualmente extraido?", "HEAD", ["origin", "tag", "stash"], "HEAD apunta a la revision actual."),
    ],
    34: [
        ("Que comando lista o crea ramas en Git?", "git branch", ["git fetch", "git push", "git log --oneline only"], "git branch gestiona ramas."),
        ("Que comando moderno cambia de rama?", "git switch", ["git init", "git tag", "git remote"], "git switch cambia entre ramas."),
        ("Que operacion integra historiales creando o no commit de fusion?", "merge", ["rebase", "stash", "tag"], "Merge combina ramas."),
        ("Que operacion reaplica commits sobre otra base?", "rebase", ["merge", "stash", "clone"], "Rebase cambia la base de una serie de commits."),
        ("Que comando guarda cambios temporalmente sin commit?", "git stash", ["git branch", "git blame", "git remote"], "git stash aparta cambios locales."),
        ("Que situacion aparece cuando Git no puede combinar cambios automaticamente?", "Conflicto", ["Fast-forward", "Tag anotado", "Clone superficial"], "Un conflicto requiere resolucion manual."),
    ],
    35: [
        ("Que nombre recibe por defecto el remoto principal al clonar un repositorio?", "origin", ["main", "HEAD", "stash"], "origin suele ser el remoto principal."),
        ("Que comando descarga cambios remotos sin fusionarlos automaticamente?", "git fetch", ["git pull", "git push", "git commit"], "fetch trae referencias remotas."),
        ("Que comando descarga e integra cambios remotos en la rama actual?", "git pull", ["git fetch", "git push", "git status"], "pull equivale a fetch mas integracion."),
        ("Que comando envia commits locales al remoto?", "git push", ["git pull", "git fetch", "git clone"], "push publica commits."),
        ("Que practica permite revisar cambios antes de integrarlos?", "Pull request", ["Rollback", "Model binding", "Certificado"], "Pull request facilita revision y validacion."),
        ("Que flujo usa ramas feature, develop, release y main/master?", "GitFlow", ["Trunk-based puro", "OData", "SCSP"], "GitFlow define varias ramas de soporte."),
    ],
    36: [
        ("Que punto electronico permite a la ciudadania acceder a servicios y tramites?", "Sede electronica", ["Indice B-tree", "RenderFragment", "Repositorio bare"], "La sede electronica es la direccion electronica de la Administracion."),
        ("Que conjunto ordenado reune documentos y actuaciones de un procedimiento?", "Expediente electronico", ["Cluster PostgreSQL", "Pull request", "Claim"], "El expediente electronico agrupa documentos y actuaciones."),
        ("Que asiento deja constancia de entrada o salida de documentos?", "Registro electronico", ["localStorage", "WAL", "DbSet"], "El registro electronico anota presentaciones."),
        ("Que codigo permite verificar la autenticidad de un documento electronico?", "CSV", ["CSS", "JWT", "WAL"], "CSV significa Codigo Seguro de Verificacion."),
        ("Que acto comunica electronicamente una resolucion o tramite al interesado?", "Notificacion electronica", ["Migracion", "Rebase", "Vacuum"], "La notificacion electronica comunica actos administrativos."),
        ("Que concepto describe la gestion completa de procedimientos por medios electronicos?", "Tramitacion electronica", ["Indexacion SQL", "Minificacion JS", "Compilacion"], "La tramitacion electronica sustituye soportes y actuaciones en papel."),
    ],
    37: [
        ("Que modulo SedipuAlba se asocia a gestion de expedientes?", "Segex", ["Sefycu", "Segra", "Secoin"], "Segex gestiona expedientes."),
        ("Que modulo SedipuAlba se asocia a firma y custodia documental?", "Sefycu", ["Segex", "Segra", "Seres"], "Sefycu se vincula con firma y custodia."),
        ("Que modulo SedipuAlba se asocia al registro?", "Segra", ["Segex", "Sefycu", "Secoin"], "Segra se relaciona con registro."),
        ("Que modulo SedipuAlba se asocia a resoluciones o servicios relacionados con tramitacion?", "Seres", ["pg_restore", "Bootstrap", "GitFlow"], "Seres forma parte de las herramientas de tramitacion SedipuAlba."),
        ("Que modulo SedipuAlba se asocia a comunicaciones internas?", "Secoin", ["Sefycu", "Segex", "AutoFirma"], "Secoin se vincula a comunicaciones internas."),
        ("Que tipo de herramientas usa un tramitador para gestionar procedimientos en SedipuAlba?", "Modulos de tramitacion", ["Indices B-tree", "Componentes Razor genericos", "Comandos Git"], "Los tramitadores trabajan con modulos de la plataforma."),
    ],
    38: [
        ("Que red conecta administraciones publicas para intercambio seguro de informacion?", "Red SARA", ["Red TOR", "Red CDN", "Red NAT privada"], "Red SARA interconecta Administraciones Publicas."),
        ("Que especificaciones permiten consultar datos de otras administraciones?", "SCSP", ["OData", "PGP", "WCAG"], "SCSP estandariza servicios de verificacion y consulta."),
        ("Que principio evita pedir al ciudadano documentos que ya obran en poder de la Administracion?", "No aportar documentos", ["Aportar siempre originales", "Duplicar expedientes", "Imprimir certificados"], "La interoperabilidad evita cargas documentales innecesarias."),
        ("Que plataforma facilita servicios de intermediacion de datos?", "PID", ["PGP", "DI", "MVC"], "PID se asocia a intermediacion y consulta de datos."),
        ("Que actuacion comprueba informacion de otra administracion sin exigir certificado al ciudadano?", "Verificacion de datos", ["Renderizado CSS", "Rebase", "Vacuum"], "La verificacion consulta datos disponibles electronicamente."),
        ("Que capacidad permite que sistemas de distintas administraciones intercambien informacion?", "Interoperabilidad", ["Polimorfismo", "Minificacion", "Indexacion"], "Interoperabilidad permite cooperacion e intercambio de datos."),
    ],
    39: [
        ("Que sistema comun permite identificacion y autenticacion ciudadana ante AAPP?", "Cl@ve", ["Bootstrap", "pg_dump", "LINQ"], "Cl@ve es plataforma comun de identificacion."),
        ("Que documento electronico de identidad permite autenticacion y firma?", "DNIe", ["CSV", "WAL", "CSS"], "DNIe incorpora certificados para identificacion y firma."),
        ("Que servicio facilita firma electronica centralizada?", "FIRe", ["SIR", "PID", "WCAG"], "FIRe integra servicios de firma."),
        ("Que espacio permite a la ciudadania consultar expedientes y notificaciones de distintas AAPP?", "Carpeta Ciudadana", ["pgAdmin", "GitHub", "Swagger"], "Carpeta Ciudadana centraliza informacion administrativa."),
        ("Que sistema se usa para intercambio registral entre administraciones?", "SIR", ["SCSS", "JWT", "B-tree"], "SIR es el Sistema de Interconexion de Registros."),
        ("Que plataforma se relaciona con intermediacion y consulta de datos?", "PID", ["PGP", "MVC", "CSS"], "PID facilita servicios de intermediacion."),
    ],
    40: [
        ("Que pautas internacionales definen criterios de accesibilidad web?", "WCAG", ["ACID", "PKI", "LINQ"], "WCAG establece pautas de accesibilidad."),
        ("Que norma europea se usa como referencia de accesibilidad TIC en el sector publico?", "UNE-EN 301549", ["ISO 9001 exclusivamente", "RDL 781/1986", "PGP"], "UNE-EN 301549 recoge requisitos de accesibilidad TIC."),
        ("Que nivel WCAG se exige habitualmente como referencia normativa en sector publico?", "AA", ["A solamente", "AAA siempre", "Beta"], "El nivel AA es la referencia habitual."),
        ("Que principio WCAG exige que la informacion pueda ser percibida por los usuarios?", "Perceptible", ["Operable", "Comprensible", "Robusto"], "Perceptible implica alternativas textuales, contraste, etc."),
        ("Que principio WCAG exige que la interfaz pueda manejarse?", "Operable", ["Perceptible", "Comprensible", "Robusto"], "Operable incluye teclado, tiempo suficiente y navegacion."),
        ("Que documento publico informa sobre el grado de cumplimiento de accesibilidad de un sitio?", "Declaracion de accesibilidad", ["Commit", "Migration", "Certificado TLS"], "Las AAPP deben publicar declaracion de accesibilidad."),
    ],
}


def _make_direct_filler_questions(target_per_topic=30):
    questions = []
    current_counts = {n: 0 for n in _TOPIC_SHORT_TITLES}
    for q in SEED_QUESTIONS:
        current_counts[q["topic_num"]] = current_counts.get(q["topic_num"], 0) + 1

    for topic_num in sorted(_TOPIC_SHORT_TITLES):
        pool = _DIRECT_POOLS[topic_num]
        needed = max(0, target_per_topic - current_counts.get(topic_num, 0))
        for idx in range(needed):
            question, answer, distractors, explanation = pool[idx % len(pool)]
            options = [answer] + list(distractors)
            shift = (topic_num + idx) % 4
            options = options[shift:] + options[:shift]
            correct = "ABCD"[options.index(answer)]
            questions.append({
                "topic_num": topic_num,
                "question": question,
                "option_a": options[0],
                "option_b": options[1],
                "option_c": options[2],
                "option_d": options[3],
                "correct": correct,
                "explanation": explanation,
            })
    return questions


SEED_QUESTIONS.extend(_make_direct_filler_questions(30))

# QUESTION_BANK_ACCEPTED_TOPIC_01_LOT_01_START
SEED_QUESTIONS.extend([
    {
        "topic_num": 1,
        "question": "¿Cuál de estas enumeraciones describe correctamente la estructura básica de la Constitución Española de 1978?",
        "option_a": "Título Preliminar, diez Títulos y disposiciones adicionales, transitorias, derogatorias y final",
        "option_b": "Doce Títulos, sin disposiciones adicionales",
        "option_c": "Un único Título dividido en capítulos",
        "option_d": "Diez Títulos, sin Título Preliminar ni disposiciones",
        "correct": "A",
        "explanation": "La estructura constitucional comprende un Título Preliminar, los Títulos I a X y disposiciones adicionales, transitorias, derogatorias y final."
    },
    {
        "topic_num": 1,
        "question": "Según el artículo 1.3 de la Constitución Española, ¿cuál es la forma política del Estado español?",
        "option_a": "República federal",
        "option_b": "Monarquía parlamentaria",
        "option_c": "Monarquía absoluta",
        "option_d": "República presidencialista",
        "correct": "B",
        "explanation": "El artículo 1.3 establece literalmente que la forma política del Estado español es la Monarquía parlamentaria."
    },
    {
        "topic_num": 1,
        "question": "¿Qué combinación recoge los principios del artículo 2 de la Constitución Española?",
        "option_a": "Unidad de la Nación, autonomía y solidaridad",
        "option_b": "Soberanía de las provincias y subsidiariedad",
        "option_c": "Confederación territorial y neutralidad",
        "option_d": "Centralización, jerarquía y uniformidad",
        "correct": "A",
        "explanation": "El artículo 2 se fundamenta en la indisoluble unidad de la Nación española y reconoce y garantiza la autonomía y la solidaridad entre sus partes."
    },
    {
        "topic_num": 1,
        "question": "Conforme al artículo 3.1 de la Constitución, ¿qué afirmación es correcta sobre el castellano?",
        "option_a": "Es la lengua oficial del Estado y todos tienen el deber de conocerla y el derecho a usarla",
        "option_b": "Solo es oficial en la Administración General del Estado",
        "option_c": "Su conocimiento es voluntario y no existe derecho de uso",
        "option_d": "Solo puede utilizarse en las relaciones privadas",
        "correct": "A",
        "explanation": "El artículo 3.1 declara el castellano lengua española oficial del Estado y establece el deber de conocerla y el derecho a usarla."
    },
    {
        "topic_num": 1,
        "question": "¿Cuál de los siguientes principios aparece expresamente en el artículo 9.3 de la Constitución Española?",
        "option_a": "Legalidad y seguridad jurídica",
        "option_b": "Censura previa de las publicaciones",
        "option_c": "Mandato imperativo de los parlamentarios",
        "option_d": "Irretroactividad de toda norma favorable",
        "correct": "A",
        "explanation": "El artículo 9.3 garantiza, entre otros, los principios de legalidad, jerarquía normativa, publicidad de las normas, irretroactividad de disposiciones sancionadoras no favorables o restrictivas, seguridad jurídica, responsabilidad e interdicción de la arbitrariedad."
    },
    {
        "topic_num": 1,
        "question": "¿Qué constituye, según el artículo 10.1, el fundamento del orden político y de la paz social?",
        "option_a": "La dignidad de la persona y el libre desarrollo de la personalidad",
        "option_b": "La potestad reglamentaria del Gobierno",
        "option_c": "La autonomía financiera provincial",
        "option_d": "La costumbre administrativa",
        "correct": "A",
        "explanation": "El artículo 10.1 sitúa la dignidad de la persona, los derechos inviolables inherentes, el libre desarrollo de la personalidad y el respeto a la ley y a los derechos ajenos como fundamento del orden político y la paz social."
    },
    {
        "topic_num": 1,
        "question": "Una norma establece un trato desfavorable por razón de nacimiento. ¿Qué parámetro constitucional resulta directamente aplicable?",
        "option_a": "La igualdad ante la ley y la prohibición de discriminación del artículo 14",
        "option_b": "La inviolabilidad del domicilio del artículo 18",
        "option_c": "La libertad de empresa del artículo 38",
        "option_d": "El derecho de petición del artículo 29",
        "correct": "A",
        "explanation": "El artículo 14 proclama la igualdad ante la ley y prohíbe la discriminación, entre otros motivos, por razón de nacimiento, raza, sexo, religión, opinión o cualquier otra condición o circunstancia personal o social."
    },
    {
        "topic_num": 1,
        "question": "¿Qué protege expresamente el artículo 15 de la Constitución Española?",
        "option_a": "La vida y la integridad física y moral",
        "option_b": "Solo la propiedad privada",
        "option_c": "La libertad de empresa frente a toda regulación",
        "option_d": "La autonomía universitaria exclusivamente",
        "correct": "A",
        "explanation": "El artículo 15 reconoce el derecho a la vida y a la integridad física y moral y prohíbe la tortura y las penas o tratos inhumanos o degradantes."
    },
    {
        "topic_num": 1,
        "question": "Según el artículo 16.2, ¿qué puede exigirse a una persona sobre su religión o creencias?",
        "option_a": "Nada: nadie puede ser obligado a declarar sobre su religión o creencias",
        "option_b": "Una declaración anual ante el Congreso",
        "option_c": "Una declaración siempre que solicite una subvención",
        "option_d": "Una declaración previa para ejercer cualquier derecho",
        "correct": "A",
        "explanation": "El artículo 16.2 dispone que nadie podrá ser obligado a declarar sobre su ideología, religión o creencias."
    },
    {
        "topic_num": 1,
        "question": "¿Cuál es el límite máximo ordinario de la detención preventiva previsto en el artículo 17.2?",
        "option_a": "24 horas en todo caso",
        "option_b": "72 horas, tras las cuales debe producirse la puesta en libertad o a disposición judicial",
        "option_c": "15 días sin control judicial",
        "option_d": "Un mes prorrogable por la policía",
        "correct": "B",
        "explanation": "El artículo 17.2 establece que la detención preventiva no puede durar más del tiempo estrictamente necesario y, en todo caso, debe finalizar en un máximo de 72 horas con libertad o puesta a disposición judicial."
    },
    {
        "topic_num": 1,
        "question": "La entrada en un domicilio sin consentimiento del titular exige, como regla constitucional, una resolución judicial o que exista flagrante delito. ¿Qué derecho fundamenta esta regla?",
        "option_a": "La inviolabilidad del domicilio del artículo 18.2",
        "option_b": "El derecho de reunión del artículo 21",
        "option_c": "El derecho de petición del artículo 29",
        "option_d": "La libertad de circulación del artículo 19",
        "correct": "A",
        "explanation": "El artículo 18.2 declara inviolable el domicilio y solo permite la entrada o registro con consentimiento del titular, resolución judicial o en caso de flagrante delito."
    },
    {
        "topic_num": 1,
        "question": "¿Qué límite establece el artículo 20.2 respecto del ejercicio de las libertades de expresión e información?",
        "option_a": "No pueden restringirse mediante ningún procedimiento judicial",
        "option_b": "No pueden someterse a ningún tipo de censura previa",
        "option_c": "Solo pueden ejercerse con autorización administrativa",
        "option_d": "Únicamente protegen comunicaciones oficiales",
        "correct": "B",
        "explanation": "El artículo 20.2 dispone que el ejercicio de estos derechos no puede restringirse mediante ningún tipo de censura previa."
    },
    {
        "topic_num": 1,
        "question": "Para una manifestación en un lugar de tránsito público, ¿qué exige el artículo 21.2 como regla general?",
        "option_a": "Autorización previa del Gobierno",
        "option_b": "Comunicación previa a la autoridad, sin autorización previa",
        "option_c": "Autorización judicial en todos los casos",
        "option_d": "Ninguna comunicación ni requisito",
        "correct": "B",
        "explanation": "El artículo 21.2 exige comunicación previa para reuniones en lugares de tránsito público y manifestaciones; no establece un régimen de autorización previa."
    },
    {
        "topic_num": 1,
        "question": "Una convocatoria para acceder a una función pública debe respetar, según el artículo 23.2, el derecho de la ciudadanía a acceder en condiciones de:",
        "option_a": "Igualdad, con los requisitos que señalen las leyes",
        "option_b": "Antigüedad sindical exclusivamente",
        "option_c": "Designación discrecional sin requisitos legales",
        "option_d": "Residencia en cualquier municipio concreto",
        "correct": "A",
        "explanation": "El artículo 23.2 reconoce el derecho a acceder en condiciones de igualdad a las funciones y cargos públicos, con los requisitos que señalen las leyes."
    },
    {
        "topic_num": 1,
        "question": "En un proceso judicial, ¿qué garantía del artículo 24.2 protege a la persona frente a la obligación de declarar contra sí misma?",
        "option_a": "El derecho a no declarar contra sí mismo y a no confesarse culpable",
        "option_b": "El derecho a elegir siempre el órgano judicial",
        "option_c": "La inmunidad parlamentaria",
        "option_d": "La potestad de dictar reglamentos",
        "correct": "A",
        "explanation": "El artículo 24.2 reconoce, entre las garantías del proceso, el derecho a no declarar contra sí mismo y a no confesarse culpable."
    },
    {
        "topic_num": 1,
        "question": "¿Qué combinación recoge el artículo 27.1 de la Constitución Española?",
        "option_a": "Derecho a la educación y libertad de enseñanza",
        "option_b": "Derecho a la educación y prohibición de toda enseñanza privada",
        "option_c": "Libertad de enseñanza sin derecho a la educación",
        "option_d": "Solo derecho de acceso a la universidad",
        "correct": "A",
        "explanation": "El artículo 27.1 reconoce el derecho de todos a la educación y la libertad de enseñanza."
    },
    {
        "topic_num": 1,
        "question": "Respecto del derecho de huelga, ¿qué prevé el artículo 28.2?",
        "option_a": "Lo reconoce para la defensa de los intereses de los trabajadores y permite regular por ley el mantenimiento de servicios esenciales",
        "option_b": "Lo prohíbe para todo el sector público",
        "option_c": "Lo somete siempre a autorización judicial individual",
        "option_d": "Lo reconoce solo para funcionarios electos",
        "correct": "A",
        "explanation": "El artículo 28.2 reconoce el derecho a la huelga para la defensa de los intereses de los trabajadores y ordena que la ley regule las garantías para asegurar el mantenimiento de los servicios esenciales de la comunidad."
    },
    {
        "topic_num": 1,
        "question": "Un sistema tributario que ignore la capacidad económica y no respete la igualdad contradice directamente el artículo:",
        "option_a": "31.1",
        "option_b": "18.3",
        "option_c": "21.1",
        "option_d": "66.3",
        "correct": "A",
        "explanation": "El artículo 31.1 exige que todos contribuyan al sostenimiento de los gastos públicos conforme a su capacidad económica, mediante un sistema tributario justo inspirado en igualdad y progresividad."
    },
    {
        "topic_num": 1,
        "question": "¿Qué órganos integran las Cortes Generales según el artículo 66.1?",
        "option_a": "Congreso de los Diputados y Senado",
        "option_b": "Gobierno y Consejo de Estado",
        "option_c": "Tribunal Constitucional y Tribunal Supremo",
        "option_d": "Congreso y Consejo General del Poder Judicial",
        "correct": "A",
        "explanation": "El artículo 66.1 establece que las Cortes Generales representan al pueblo español y están formadas por el Congreso de los Diputados y el Senado."
    },
    {
        "topic_num": 1,
        "question": "¿Qué mayoría exige el artículo 81.2 para aprobar, modificar o derogar una ley orgánica?",
        "option_a": "Mayoría simple del Senado",
        "option_b": "Mayoría absoluta del Congreso en una votación final sobre el conjunto del proyecto",
        "option_c": "Unanimidad de las Cortes Generales",
        "option_d": "Mayoría de tres quintos de ambas Cámaras en dos votaciones",
        "correct": "B",
        "explanation": "El artículo 81.2 exige mayoría absoluta del Congreso, en una votación final sobre el conjunto del proyecto, para aprobar, modificar o derogar leyes orgánicas."
    }
])
# QUESTION_BANK_ACCEPTED_TOPIC_01_LOT_01_END

# QUESTION_BANK_ACCEPTED_TOPIC_02_LOT_01_START
SEED_QUESTIONS.extend([
    {
        "topic_num": 2,
        "question": "¿Qué función constitucional corresponde al Gobierno conforme al artículo 97?",
        "option_a": "Dirigir la política interior y exterior, la Administración civil y militar y la defensa del Estado",
        "option_b": "Ejercer exclusivamente la potestad legislativa",
        "option_c": "Controlar directamente a los jueces y tribunales",
        "option_d": "Aprobar los Estatutos de Autonomía sin intervención parlamentaria",
        "correct": "A",
        "explanation": "El artículo 97 atribuye al Gobierno la dirección de la política interior y exterior, de la Administración civil y militar y de la defensa del Estado, además de la función ejecutiva y la potestad reglamentaria."
    },
    {
        "topic_num": 2,
        "question": "¿Quiénes componen el Gobierno según el artículo 98.1 de la Constitución?",
        "option_a": "Presidente, Vicepresidentes en su caso, Ministros y demás miembros que establezca la ley",
        "option_b": "Solo Presidente y Ministros, sin posibilidad de Vicepresidentes",
        "option_c": "Presidente, Congreso y Senado",
        "option_d": "Rey, Presidente y Ministros",
        "correct": "A",
        "explanation": "El Gobierno se compone del Presidente, de los Vicepresidentes en su caso, de los Ministros y de los demás miembros que establezca la ley."
    },
    {
        "topic_num": 2,
        "question": "¿Qué relación establece el artículo 98.2 entre el Presidente del Gobierno y los Ministros?",
        "option_a": "El Presidente dirige la acción del Gobierno y coordina las funciones de sus miembros, sin perjuicio de la competencia y responsabilidad directa de estos",
        "option_b": "Los Ministros dirigen al Presidente mediante mandato imperativo",
        "option_c": "El Presidente solo representa al Gobierno, pero no coordina sus funciones",
        "option_d": "El Congreso ejerce las funciones directas de cada Ministro",
        "correct": "A",
        "explanation": "El artículo 98.2 distingue la dirección y coordinación del Presidente de la competencia y responsabilidad directa de los Ministros en su gestión."
    },
    {
        "topic_num": 2,
        "question": "¿Qué regla de incompatibilidad se aplica a los miembros del Gobierno?",
        "option_a": "No pueden ejercer otras funciones representativas que las propias del mandato parlamentario ni otra función pública no derivada de su cargo, ni actividad profesional o mercantil",
        "option_b": "Pueden ejercer cualquier actividad mercantil si la comunica al Congreso",
        "option_c": "Solo tienen prohibido ser diputados o senadores",
        "option_d": "La Constitución no establece incompatibilidades para ellos",
        "correct": "A",
        "explanation": "El artículo 98.3 establece esa incompatibilidad, con la excepción de las funciones representativas propias del mandato parlamentario."
    },
    {
        "topic_num": 2,
        "question": "¿Quién nombra y separa a los Ministros?",
        "option_a": "El Congreso, por mayoría absoluta",
        "option_b": "El Rey, a propuesta del Presidente del Gobierno",
        "option_c": "El Presidente del Congreso, a propuesta del Senado",
        "option_d": "El Tribunal Constitucional",
        "correct": "B",
        "explanation": "El artículo 100 dispone que los demás miembros del Gobierno son nombrados y separados por el Rey, a propuesta de su Presidente."
    },
    {
        "topic_num": 2,
        "question": "¿Ante qué Cámara es políticamente responsable el Gobierno en su conjunto?",
        "option_a": "Ante el Senado exclusivamente",
        "option_b": "Ante el Congreso de los Diputados",
        "option_c": "Ante el Tribunal Constitucional",
        "option_d": "Ante las Asambleas legislativas autonómicas",
        "correct": "B",
        "explanation": "El artículo 108 establece que el Gobierno responde solidariamente en su gestión política ante el Congreso de los Diputados."
    },
    {
        "topic_num": 2,
        "question": "Respecto de la responsabilidad criminal del Presidente y los Ministros, ¿qué afirmación es constitucionalmente correcta?",
        "option_a": "La acusación por traición o delito contra la seguridad del Estado solo puede plantearse por iniciativa de la cuarta parte del Congreso y con aprobación de mayoría absoluta",
        "option_b": "La acusación puede iniciarla cualquier senador y exige mayoría simple del Senado",
        "option_c": "La responsabilidad criminal se exige siempre ante el Tribunal Constitucional",
        "option_d": "La Constitución permite el indulto de la responsabilidad por traición",
        "correct": "A",
        "explanation": "El artículo 102 exige iniciativa de la cuarta parte del Congreso y aprobación por mayoría absoluta para esa acusación; no procede la prerrogativa real de gracia en el caso de traición."
    },
    {
        "topic_num": 2,
        "question": "¿Qué instrumento parlamentario permite a un diputado o senador solicitar explicaciones al Gobierno sobre un asunto?",
        "option_a": "Preguntas e interpelaciones, en los términos que establezcan los Reglamentos parlamentarios",
        "option_b": "Solo mociones de censura",
        "option_c": "Exclusivamente decretos legislativos",
        "option_d": "Únicamente recursos de amparo",
        "correct": "A",
        "explanation": "El artículo 111 prevé que el Gobierno y cada uno de sus miembros están sometidos a las interpelaciones y preguntas que se les formulen en las Cámaras."
    },
    {
        "topic_num": 2,
        "question": "¿Quién puede plantear la cuestión de confianza?",
        "option_a": "El Presidente del Gobierno, previa deliberación del Consejo de Ministros",
        "option_b": "Cualquier Ministro sin deliberación previa",
        "option_c": "El Rey por iniciativa propia",
        "option_d": "El Senado sin intervención del Gobierno",
        "correct": "A",
        "explanation": "Conforme al artículo 112, el Presidente del Gobierno, previa deliberación del Consejo de Ministros, puede plantear ante el Congreso la cuestión de confianza sobre su programa o una declaración de política general."
    },
    {
        "topic_num": 2,
        "question": "¿Qué requisito singular caracteriza la moción de censura constitucional?",
        "option_a": "Debe incluir un candidato a la Presidencia del Gobierno",
        "option_b": "Debe ser presentada por todos los diputados",
        "option_c": "Debe aprobarse siempre por el Senado",
        "option_d": "No puede someterse a votación",
        "correct": "A",
        "explanation": "El artículo 113 configura la moción de censura como constructiva: debe ser propuesta al menos por la décima parte de los diputados e incluir un candidato a la Presidencia."
    },
    {
        "topic_num": 2,
        "question": "¿Cuál es la diferencia constitucional básica entre cuestión de confianza y moción de censura?",
        "option_a": "La primera la plantea el Presidente sobre su programa o política general; la segunda es propuesta por diputados e incluye candidato alternativo",
        "option_b": "Ambas las plantea el Rey y se votan solo en el Senado",
        "option_c": "La cuestión de confianza sustituye siempre al control judicial",
        "option_d": "La moción de censura no afecta a la responsabilidad política del Gobierno",
        "correct": "A",
        "explanation": "Los artículos 112 y 113 regulan mecanismos distintos: iniciativa presidencial en la confianza e iniciativa parlamentaria constructiva en la censura."
    },
    {
        "topic_num": 2,
        "question": "¿Qué límite se aplica a la propuesta de disolución de las Cámaras por el Presidente del Gobierno?",
        "option_a": "No puede proponerse mientras esté en trámite una moción de censura",
        "option_b": "Puede proponerse durante una moción de censura si lo autoriza el Rey",
        "option_c": "Solo puede acordarla el Senado",
        "option_d": "Debe aprobarla previamente el Tribunal Constitucional",
        "correct": "A",
        "explanation": "El artículo 115 impide presentar propuesta de disolución mientras esté en trámite una moción de censura."
    },
    {
        "topic_num": 2,
        "question": "¿Qué entidades territoriales se organizan constitucionalmente y gozan de autonomía para la gestión de sus respectivos intereses?",
        "option_a": "Municipios, provincias y Comunidades Autónomas",
        "option_b": "Solo Comunidades Autónomas",
        "option_c": "Solo municipios y comarcas",
        "option_d": "Ministerios y provincias exclusivamente",
        "correct": "A",
        "explanation": "El artículo 137 organiza territorialmente el Estado en municipios, provincias y Comunidades Autónomas, todas dotadas de autonomía para la gestión de sus intereses."
    },
    {
        "topic_num": 2,
        "question": "¿Cómo se gobiernan y administran los municipios según el artículo 140?",
        "option_a": "Por Ayuntamientos integrados por Alcaldes y Concejales",
        "option_b": "Por delegados del Gobierno sin autonomía",
        "option_c": "Por las Diputaciones Provinciales directamente",
        "option_d": "Por órganos judiciales",
        "correct": "A",
        "explanation": "El artículo 140 garantiza la autonomía municipal y dispone que el gobierno y administración de los municipios corresponde a sus respectivos Ayuntamientos, integrados por Alcaldes y Concejales."
    },
    {
        "topic_num": 2,
        "question": "¿Qué definición constitucional corresponde a la provincia?",
        "option_a": "Entidad local con personalidad jurídica propia determinada por la agrupación de municipios y división territorial para el cumplimiento de actividades del Estado",
        "option_b": "Órgano desconcentrado del Gobierno sin personalidad jurídica",
        "option_c": "Agrupación voluntaria de Comunidades Autónomas",
        "option_d": "Entidad creada exclusivamente para fines electorales",
        "correct": "A",
        "explanation": "El artículo 141 define la provincia como entidad local con personalidad jurídica propia, determinada por la agrupación de municipios, y como división territorial para actividades del Estado."
    },
    {
        "topic_num": 2,
        "question": "¿Qué exige la Constitución respecto de las Haciendas locales?",
        "option_a": "Disponer de medios suficientes para el desempeño de las funciones que la ley atribuye a las Corporaciones respectivas",
        "option_b": "Financiarse únicamente con tasas municipales",
        "option_c": "Depender exclusivamente de transferencias estatales sin tributos propios",
        "option_d": "Carecer de participación en tributos estatales y autonómicos",
        "correct": "A",
        "explanation": "El artículo 142 exige que las Haciendas locales dispongan de medios suficientes y prevé que se nutran de tributos propios y participación en los del Estado y las Comunidades Autónomas."
    },
    {
        "topic_num": 2,
        "question": "¿Cuál de estos contenidos debe figurar en un Estatuto de Autonomía?",
        "option_a": "La denominación, organización y sede de las instituciones autónomas propias",
        "option_b": "La composición del Tribunal Supremo",
        "option_c": "La regulación completa de la defensa nacional",
        "option_d": "La fijación anual de los Presupuestos Generales del Estado",
        "correct": "A",
        "explanation": "El artículo 147.2 incluye, entre otros contenidos, la denominación de la Comunidad, su territorio, la denominación, organización y sede de sus instituciones autónomas propias y las competencias asumidas."
    },
    {
        "topic_num": 2,
        "question": "¿Qué afirmación refleja la distribución constitucional de competencias?",
        "option_a": "Las materias no atribuidas expresamente al Estado pueden corresponder a las Comunidades Autónomas según sus Estatutos, y el derecho estatal es supletorio",
        "option_b": "Toda competencia no enumerada corresponde siempre al Estado",
        "option_c": "Las Comunidades Autónomas pueden asumir cualquier competencia sin Estatuto",
        "option_d": "El derecho autonómico prevalece siempre sobre el estatal",
        "correct": "A",
        "explanation": "El artículo 149.3 establece la cláusula residual a favor de las Comunidades Autónomas en los términos indicados, la prevalencia del derecho estatal en caso de conflicto fuera de la competencia exclusiva autonómica y su carácter supletorio."
    },
    {
        "topic_num": 2,
        "question": "¿Qué control corresponde al Tribunal Constitucional sobre disposiciones normativas con fuerza de ley de las Comunidades Autónomas?",
        "option_a": "El control de su constitucionalidad",
        "option_b": "El control de oportunidad política",
        "option_c": "La aprobación previa de cada reglamento autonómico",
        "option_d": "La dirección ordinaria de la Administración autonómica",
        "correct": "A",
        "explanation": "El artículo 153.a atribuye al Tribunal Constitucional el control de la constitucionalidad de las disposiciones normativas con fuerza de ley de las Comunidades Autónomas."
    },
    {
        "topic_num": 2,
        "question": "Para adoptar medidas del artículo 155 frente a una Comunidad Autónoma incumplidora, ¿qué requisito parlamentario se exige?",
        "option_a": "La aprobación por mayoría absoluta del Senado, después del requerimiento al Presidente autonómico",
        "option_b": "La aprobación por mayoría simple del Congreso sin requerimiento",
        "option_c": "La autorización del Tribunal Supremo",
        "option_d": "La aprobación unánime de todas las Comunidades Autónomas",
        "correct": "A",
        "explanation": "El artículo 155 exige requerimiento previo al Presidente de la Comunidad y, si no es atendido, aprobación por mayoría absoluta del Senado para adoptar las medidas previstas."
    }
])
# QUESTION_BANK_ACCEPTED_TOPIC_02_LOT_01_END

# QUESTION_BANK_ACCEPTED_TOPIC_03_LOT_01_START
SEED_QUESTIONS.extend([
    {
        "topic_num": 3,
        "question": "¿Qué es el municipio según la Ley 7/1985?",
        "option_a": "La entidad local básica de la organización territorial del Estado",
        "option_b": "Un órgano desconcentrado de la provincia",
        "option_c": "Una unidad administrativa sin personalidad jurídica",
        "option_d": "Una asociación privada de vecinos",
        "correct": "A",
        "explanation": "El artículo 11 define el municipio como la entidad local básica de la organización territorial del Estado, con personalidad jurídica y plena capacidad para el cumplimiento de sus fines."
    },
    {
        "topic_num": 3,
        "question": "¿Cuáles son los elementos del municipio?",
        "option_a": "El territorio, la población y la organización",
        "option_b": "El presupuesto, la provincia y el Gobierno",
        "option_c": "El padrón, el Pleno y el Senado",
        "option_d": "El territorio, el Parlamento y la Administración estatal",
        "correct": "A",
        "explanation": "El artículo 11.2 identifica como elementos del municipio el territorio, la población y la organización."
    },
    {
        "topic_num": 3,
        "question": "¿Qué regla territorial establece la Ley 7/1985 para los municipios?",
        "option_a": "Cada municipio pertenece a una sola provincia",
        "option_b": "Un municipio puede pertenecer simultáneamente a varias provincias",
        "option_c": "Todos los municipios deben formar una comarca",
        "option_d": "La pertenencia provincial depende del padrón anual",
        "correct": "A",
        "explanation": "El artículo 12.2 establece que cada municipio pertenecerá a una sola provincia."
    },
    {
        "topic_num": 3,
        "question": "¿Qué instrumento acredita la residencia y el domicilio habitual en un municipio?",
        "option_a": "El padrón municipal",
        "option_b": "El registro de intereses de los concejales",
        "option_c": "El presupuesto municipal",
        "option_d": "El plan provincial de cooperación",
        "correct": "A",
        "explanation": "El padrón municipal es el registro administrativo donde constan los vecinos del municipio y sus datos constituyen prueba de la residencia y del domicilio habitual en él."
    },
    {
        "topic_num": 3,
        "question": "¿Qué órganos existen en todos los Ayuntamientos?",
        "option_a": "Alcalde, Tenientes de Alcalde y Pleno",
        "option_b": "Solo Alcalde y Junta de Gobierno Local",
        "option_c": "Presidente provincial y Pleno autonómico",
        "option_d": "Alcalde, Senado y Consejo de Estado",
        "correct": "A",
        "explanation": "El artículo 20.1.a dispone que el Alcalde, los Tenientes de Alcalde y el Pleno existen en todos los Ayuntamientos."
    },
    {
        "topic_num": 3,
        "question": "¿Cuándo existe la Junta de Gobierno Local conforme a la regla general del artículo 20.1.b?",
        "option_a": "En municipios con población superior a 5.000 habitantes y en los de menos cuando lo disponga el reglamento orgánico o lo acuerde el Pleno",
        "option_b": "Solo en municipios capitales de provincia",
        "option_c": "En todos los municipios sin excepción",
        "option_d": "Solo cuando lo ordene la Diputación",
        "correct": "A",
        "explanation": "La Junta de Gobierno Local existe en todos los municipios con población superior a 5.000 habitantes y en los de menos cuando concurra alguno de los supuestos legales indicados."
    },
    {
        "topic_num": 3,
        "question": "¿Qué función corresponde al Alcalde como órgano municipal?",
        "option_a": "Dirigir el gobierno y la administración municipal y representar al Ayuntamiento",
        "option_b": "Controlar la constitucionalidad de las leyes",
        "option_c": "Aprobar los Estatutos de Autonomía",
        "option_d": "Nombrar a los jueces del partido judicial",
        "correct": "A",
        "explanation": "El artículo 21.1 atribuye al Alcalde la dirección del gobierno y la administración municipal y la representación del Ayuntamiento, entre otras funciones."
    },
    {
        "topic_num": 3,
        "question": "¿Qué función tiene el Pleno respecto del gobierno municipal?",
        "option_a": "El control y la fiscalización de los órganos de gobierno",
        "option_b": "La dirección ordinaria de todos los servicios estatales",
        "option_c": "La elección de los diputados provinciales por sufragio directo",
        "option_d": "La aprobación de sentencias",
        "correct": "A",
        "explanation": "El artículo 22.2.a atribuye al Pleno el control y la fiscalización de los órganos de gobierno."
    },
    {
        "topic_num": 3,
        "question": "¿Cuál de estas materias corresponde al Pleno municipal?",
        "option_a": "La aprobación del reglamento orgánico y de las ordenanzas",
        "option_b": "La representación legal ordinaria del municipio",
        "option_c": "La jefatura superior de todo el personal por delegación automática",
        "option_d": "La convocatoria de todas las sesiones de la Junta de Gobierno Local",
        "correct": "A",
        "explanation": "El artículo 22.2.d atribuye al Pleno la aprobación del reglamento orgánico y de las ordenanzas, sin perjuicio de otras competencias enumeradas."
    },
    {
        "topic_num": 3,
        "question": "¿Cuál es la función propia de la Junta de Gobierno Local?",
        "option_a": "Asistir al Alcalde en el ejercicio de sus atribuciones y ejercer las atribuciones que le deleguen o atribuyan las leyes",
        "option_b": "Sustituir siempre al Pleno en sus funciones de control",
        "option_c": "Aprobar leyes estatales",
        "option_d": "Resolver recursos de inconstitucionalidad",
        "correct": "A",
        "explanation": "El artículo 23.2 establece que la Junta de Gobierno Local asiste al Alcalde y ejerce las atribuciones que el Alcalde u otro órgano le delegue o le atribuyan las leyes."
    },
    {
        "topic_num": 3,
        "question": "¿Cómo define la Ley 7/1985 a la provincia?",
        "option_a": "Entidad local determinada por la agrupación de municipios, con personalidad jurídica propia, y división territorial para actividades del Estado",
        "option_b": "Órgano sin personalidad jurídica de la Comunidad Autónoma",
        "option_c": "Agrupación de concejales de un municipio",
        "option_d": "Unidad administrativa creada por cada Ayuntamiento",
        "correct": "A",
        "explanation": "El artículo 31 define la provincia en esos términos y reconoce su autonomía para la gestión de sus intereses."
    },
    {
        "topic_num": 3,
        "question": "¿Qué órganos son necesarios en todas las Diputaciones?",
        "option_a": "Presidente, Vicepresidentes, Junta de Gobierno y Pleno",
        "option_b": "Solo Presidente y Pleno",
        "option_c": "Alcalde, Senado y Junta Electoral",
        "option_d": "Delegado del Gobierno y Consejo de Ministros",
        "correct": "A",
        "explanation": "El artículo 32.1 establece como órganos necesarios de la Diputación el Presidente, los Vicepresidentes, la Junta de Gobierno y el Pleno."
    },
    {
        "topic_num": 3,
        "question": "¿Qué función corresponde al Presidente de la Diputación?",
        "option_a": "Dirigir el gobierno y la administración de la provincia y representar a la Diputación",
        "option_b": "Aprobar unilateralmente leyes orgánicas",
        "option_c": "Designar a los Alcaldes de todos los municipios",
        "option_d": "Resolver los recursos contencioso-administrativos",
        "correct": "A",
        "explanation": "El artículo 34.1 atribuye al Presidente la dirección del gobierno y la administración de la provincia y la representación de la Diputación, entre otras competencias."
    },
    {
        "topic_num": 3,
        "question": "¿Qué función de control corresponde al Pleno de la Diputación?",
        "option_a": "El control y la fiscalización de los órganos de gobierno",
        "option_b": "La aprobación de sentencias provinciales",
        "option_c": "La dirección de la Administración General del Estado",
        "option_d": "La elección directa de todos los concejales",
        "correct": "A",
        "explanation": "El artículo 33.2.a atribuye al Pleno provincial el control y la fiscalización de los órganos de gobierno."
    },
    {
        "topic_num": 3,
        "question": "¿Qué asistencia debe prestar la Diputación a los municipios?",
        "option_a": "Asistencia y cooperación jurídica, económica y técnica, especialmente a los municipios de menor capacidad económica y de gestión",
        "option_b": "Solo asistencia protocolaria a los municipios capitales",
        "option_c": "Únicamente financiación de obras estatales",
        "option_d": "Asistencia exclusiva en materia electoral",
        "correct": "A",
        "explanation": "El artículo 36.1.b atribuye a la Diputación la asistencia y cooperación jurídica, económica y técnica a los municipios, especialmente a los de menor capacidad."
    },
    {
        "topic_num": 3,
        "question": "¿Qué competencia provincial se refiere a los servicios municipales entre sí?",
        "option_a": "La coordinación de los servicios municipales para garantizar una prestación integral y adecuada",
        "option_b": "La aprobación de los planes urbanísticos estatales",
        "option_c": "La dirección de los órganos judiciales",
        "option_d": "La imposición de sanciones penales",
        "correct": "A",
        "explanation": "El artículo 36.1.a atribuye a la Diputación la coordinación de los servicios municipales entre sí para garantizar la prestación integral y adecuada."
    },
    {
        "topic_num": 3,
        "question": "¿Qué tipo de servicios puede prestar la Diputación conforme al artículo 36.1.c?",
        "option_a": "Servicios públicos de carácter supramunicipal y, en su caso, supracomarcal",
        "option_b": "Solo servicios internos de la Diputación",
        "option_c": "Exclusivamente servicios de competencia estatal",
        "option_d": "Servicios privados sin relación con los municipios",
        "correct": "A",
        "explanation": "El artículo 36.1.c incluye la prestación de servicios públicos de carácter supramunicipal y, en su caso, supracomarcal, además del fomento o coordinación de prestación unificada."
    },
    {
        "topic_num": 3,
        "question": "¿Qué instrumento provincial debe aprobarse anualmente para cooperar en obras y servicios municipales?",
        "option_a": "Un plan provincial de cooperación a las obras y servicios de competencia municipal",
        "option_b": "Un reglamento estatal de personal",
        "option_c": "Un Estatuto de Autonomía provincial",
        "option_d": "Un decreto judicial de servicios",
        "correct": "A",
        "explanation": "El artículo 36.2.a prevé la aprobación anual de un plan provincial de cooperación, elaborado con participación de los municipios."
    },
    {
        "topic_num": 3,
        "question": "¿Qué finalidad tiene la asistencia provincial respecto de los servicios mínimos municipales?",
        "option_a": "Asegurar el acceso de la población al conjunto de los servicios mínimos y la mayor eficacia y economía en su prestación",
        "option_b": "Sustituir siempre a los Ayuntamientos en toda competencia",
        "option_c": "Eliminar la autonomía municipal",
        "option_d": "Financiar exclusivamente actividades privadas",
        "correct": "A",
        "explanation": "El artículo 36.2.b encomienda a la Diputación asegurar el acceso de la población provincial al conjunto de los servicios mínimos de competencia municipal y la mayor eficacia y economía en su prestación."
    },
    {
        "topic_num": 3,
        "question": "¿Qué relación describe correctamente la organización municipal y provincial?",
        "option_a": "Ambas son entidades locales con órganos propios y autonomía para gestionar sus intereses, dentro del marco legal",
        "option_b": "La provincia dirige jerárquicamente a todos los Ayuntamientos",
        "option_c": "El municipio carece de personalidad jurídica propia",
        "option_d": "La Diputación es un órgano del Gobierno de la Nación",
        "correct": "A",
        "explanation": "La Ley 7/1985 reconoce personalidad y autonomía a municipios y provincias, y regula sus órganos y competencias sin convertir la provincia en superior jerárquico general de los Ayuntamientos."
    }
])
# QUESTION_BANK_ACCEPTED_TOPIC_03_LOT_01_END

# QUESTION_BANK_ACCEPTED_TOPIC_04_LOT_01_START
SEED_QUESTIONS.extend([
    {
        "topic_num": 4,
        "question": "¿Ante quién se exige la responsabilidad civil y penal de los miembros de las Corporaciones Locales?",
        "option_a": "Ante los Tribunales de Justicia competentes, por el procedimiento ordinario aplicable",
        "option_b": "Ante el Pleno, sin intervención judicial",
        "option_c": "Ante la Diputación Provincial en vía administrativa",
        "option_d": "Ante el Senado",
        "correct": "A",
        "explanation": "El artículo 22.3 del texto refundido dispone que la responsabilidad se exigirá ante los Tribunales de Justicia competentes y se tramitará por el procedimiento ordinario aplicable."
    },
    {
        "topic_num": 4,
        "question": "¿Cuándo debe abstenerse un miembro de una Corporación Local?",
        "option_a": "Cuando concurra una causa de abstención prevista en la legislación de procedimiento administrativo o de contratos públicos",
        "option_b": "Solo cuando lo ordene el Alcalde",
        "option_c": "Únicamente en asuntos presupuestarios",
        "option_d": "Nunca, porque el cargo electo no puede abstenerse",
        "correct": "A",
        "explanation": "El artículo 21 obliga a abstenerse de deliberar, votar, decidir y ejecutar cuando concurra una causa legal de incompatibilidad o abstención."
    },
    {
        "topic_num": 4,
        "question": "¿Cómo se constituyen los miembros de las Corporaciones Locales a efectos de su actuación corporativa?",
        "option_a": "En grupos, sin que nadie pueda pertenecer simultáneamente a más de uno",
        "option_b": "En un único grupo obligatorio sin portavoz",
        "option_c": "En grupos designados por el Gobierno",
        "option_d": "Individualmente, sin posibilidad de grupos",
        "correct": "A",
        "explanation": "El artículo 23 dispone que los miembros se constituirán en grupos y que nadie puede pertenecer simultáneamente a más de uno."
    },
    {
        "topic_num": 4,
        "question": "¿A quién se dirige el escrito de constitución de un grupo político local?",
        "option_a": "Al Presidente, suscrito por todos sus integrantes y presentado en la Secretaría General dentro de los cinco días hábiles siguientes a la constitución",
        "option_b": "Al Rey dentro de los treinta días naturales",
        "option_c": "Al Delegado del Gobierno sin firma de sus integrantes",
        "option_d": "Al Secretario judicial en cualquier momento",
        "correct": "A",
        "explanation": "El artículo 24.1 exige escrito dirigido al Presidente y suscrito por todos los integrantes, presentado en Secretaría General dentro de los cinco días hábiles siguientes a la constitución."
    },
    {
        "topic_num": 4,
        "question": "¿Quién tiene la custodia y dirección del Registro de Intereses de los miembros de la Corporación?",
        "option_a": "El Secretario de la Corporación",
        "option_b": "El Presidente del Gobierno",
        "option_c": "El portavoz del grupo mayoritario",
        "option_d": "El Delegado del Gobierno",
        "correct": "A",
        "explanation": "El artículo 30.1 atribuye la custodia y dirección del Registro de Intereses al Secretario."
    },
    {
        "topic_num": 4,
        "question": "Si varían las circunstancias declaradas en el Registro de Intereses, ¿qué plazo tiene el miembro de la Corporación para comunicar la variación?",
        "option_a": "Un mes desde el día en que se produjo la variación",
        "option_b": "Cinco días hábiles desde la sesión plenaria",
        "option_c": "Un año desde la toma de posesión",
        "option_d": "No existe plazo",
        "correct": "A",
        "explanation": "El artículo 30.2.b fija un mes desde el día en que se hayan producido las variaciones."
    },
    {
        "topic_num": 4,
        "question": "¿Qué órganos son necesarios en un Ayuntamiento conforme al artículo 35 del texto refundido?",
        "option_a": "Alcalde, Tenientes de Alcalde, Pleno y Comisión de Gobierno en los supuestos previstos",
        "option_b": "Presidente provincial, Senado y Pleno autonómico",
        "option_c": "Solo Alcalde y Secretario",
        "option_d": "Alcalde y Tribunal de Cuentas",
        "correct": "A",
        "explanation": "El artículo 35 enumera como órganos necesarios el Alcalde, los Tenientes de Alcalde, el Pleno y la Comisión de Gobierno en los municipios y supuestos que indica."
    },
    {
        "topic_num": 4,
        "question": "¿Cuándo es necesaria la Comisión de Gobierno según el artículo 35.2.d del texto refundido?",
        "option_a": "En municipios con población de derecho superior a 5.000 habitantes y, en los de menos, cuando lo disponga el reglamento orgánico o lo acuerde el Pleno",
        "option_b": "Solo en municipios de menos de 5.000 habitantes",
        "option_c": "En todos los municipios sin excepción",
        "option_d": "Solo cuando lo solicite la Diputación",
        "correct": "A",
        "explanation": "El artículo 35.2.d establece ese umbral y las dos vías alternativas para municipios de menor población."
    },
    {
        "topic_num": 4,
        "question": "¿Qué órganos enumera el artículo 32 del texto refundido para la provincia?",
        "option_a": "Presidente, Vicepresidentes, Comisión de Gobierno y Pleno",
        "option_b": "Alcalde, Tenientes y Senado",
        "option_c": "Solo Presidente y Secretario",
        "option_d": "Delegado del Gobierno y Tribunal Superior de Justicia",
        "correct": "A",
        "explanation": "El artículo 32 enumera Presidente, Vicepresidentes, Comisión de Gobierno y Pleno como órganos de la provincia, con las reglas que establece."
    },
    {
        "topic_num": 4,
        "question": "¿Qué tratamiento corresponde a los Presidentes de las Diputaciones Provinciales según el artículo 34?",
        "option_a": "Excelencia al de la Diputación de Barcelona e Ilustrísima a los de las demás Diputaciones",
        "option_b": "Siempre Señoría sin excepciones",
        "option_c": "Siempre Excelencia para todas las Diputaciones",
        "option_d": "El tratamiento del Alcalde del municipio sede",
        "correct": "A",
        "explanation": "El artículo 34.1 atribuye tratamiento de Excelencia al Presidente de la Diputación de Barcelona y de Ilustrísima a los de las demás Diputaciones."
    },
    {
        "topic_num": 4,
        "question": "¿Quién designa representantes de un grupo político en órganos colegiados integrados por miembros de varios grupos?",
        "option_a": "El grupo político, mediante escrito de su portavoz dirigido al Presidente",
        "option_b": "El Secretario de Estado de Administraciones Públicas",
        "option_c": "El Tribunal Constitucional",
        "option_d": "El grupo político más votado de otra Corporación",
        "correct": "A",
        "explanation": "El artículo 29 atribuye esa designación a los grupos políticos mediante escrito de su portavoz dirigido al Presidente."
    },
    {
        "topic_num": 4,
        "question": "¿Qué se necesita para acceder a los datos del Registro de Intereses?",
        "option_a": "Acreditar la condición legal de interesado legítimo directo conforme a la legislación aplicable",
        "option_b": "La autorización de cualquier concejal",
        "option_c": "La autorización del Gobierno de la Nación en todo caso",
        "option_d": "Ningún requisito",
        "correct": "A",
        "explanation": "El artículo 32 exige acreditar la condición legal de interesado legítimo directo con arreglo a la legislación autonómica o estatal aplicable."
    },
    {
        "topic_num": 4,
        "question": "¿A qué órgano da cuenta el Presidente de la constitución de los grupos políticos?",
        "option_a": "Al Pleno, en la primera sesión que se celebre después de cumplirse el plazo legal",
        "option_b": "A la Junta de Gobierno de la Comunidad Autónoma",
        "option_c": "Al Senado en la sesión siguiente",
        "option_d": "Al Tribunal de Cuentas",
        "correct": "A",
        "explanation": "El artículo 25 dispone que el Presidente dará cuenta al Pleno en la primera sesión celebrada tras cumplirse el plazo del artículo 24.1."
    },
    {
        "topic_num": 4,
        "question": "¿Qué debe hacer un miembro de la Corporación que adquiere su condición después de la sesión constitutiva?",
        "option_a": "Incorporarse a los grupos conforme a las reglas acordadas por la Corporación",
        "option_b": "Actuar siempre sin grupo político",
        "option_c": "Solicitar autorización al Senado",
        "option_d": "Formar automáticamente un grupo propio",
        "correct": "A",
        "explanation": "El artículo 26 exige la incorporación a los grupos conforme a las reglas acordadas por la Corporación."
    },
    {
        "topic_num": 4,
        "question": "¿Qué medios pueden poner las Corporaciones Locales a disposición de los grupos políticos?",
        "option_a": "Un despacho o local para reunirse y recibir visitas, junto con una infraestructura mínima según las posibilidades funcionales",
        "option_b": "Solo vehículos oficiales para cada miembro",
        "option_c": "Únicamente una cuenta bancaria privada",
        "option_d": "Ningún medio material o personal",
        "correct": "A",
        "explanation": "El artículo 27 prevé despacho o local e infraestructura mínima de medios materiales y personales en la medida de las posibilidades funcionales de la organización administrativa."
    },
    {
        "topic_num": 4,
        "question": "¿Qué límite establece el artículo 28.3 para las reuniones de grupos políticos en locales corporativos?",
        "option_a": "No pueden coincidir con sesiones del Pleno o de la Comisión de Gobierno",
        "option_b": "Solo pueden celebrarse durante sesiones del Pleno",
        "option_c": "Deben celebrarse siempre fuera de la sede",
        "option_d": "No existe límite temporal",
        "correct": "A",
        "explanation": "El artículo 28.3 prohíbe que esas reuniones coincidan con sesiones del Pleno o de la Comisión de Gobierno."
    },
    {
        "topic_num": 4,
        "question": "¿Qué debe incluir necesariamente la declaración de intereses?",
        "option_a": "La identificación de bienes, actividades y ocupaciones profesionales o privadas y otros intereses relacionados con las competencias corporativas",
        "option_b": "Solo la declaración de bienes inmuebles",
        "option_c": "Únicamente la afiliación política",
        "option_d": "Solo las retribuciones públicas",
        "correct": "A",
        "explanation": "El artículo 31 incluye bienes muebles e inmuebles, actividades y ocupaciones y otros intereses o actividades privadas relacionados con las competencias de la Corporación."
    },
    {
        "topic_num": 4,
        "question": "¿Qué carácter tiene el Ayuntamiento según el artículo 35.1 del texto refundido?",
        "option_a": "Es el órgano de gobierno y administración del municipio, con carácter de Corporación de Derecho Público",
        "option_b": "Es un órgano consultivo de la Diputación",
        "option_c": "Es una empresa pública estatal",
        "option_d": "Es una asociación privada sin personalidad",
        "correct": "A",
        "explanation": "El artículo 35.1 define al Ayuntamiento como órgano de gobierno y administración del municipio, con carácter de Corporación de Derecho Público."
    },
    {
        "topic_num": 4,
        "question": "¿Qué regla especial se aplica a los Presidentes de Cabildos y Consejos Insulares?",
        "option_a": "Ostentan el mismo tratamiento, deberes y derechos reconocidos a los Presidentes de Diputación",
        "option_b": "Carecen de tratamiento institucional",
        "option_c": "Tienen siempre el tratamiento de Excelencia",
        "option_d": "Solo pueden ejercer funciones consultivas",
        "correct": "A",
        "explanation": "El artículo 34.2 extiende a los Presidentes de Cabildos y Consejos Insulares el mismo tratamiento, deberes y derechos reconocidos a los Presidentes de Diputación."
    },
    {
        "topic_num": 4,
        "question": "¿Qué afirmación distingue correctamente los artículos 24 y 30 del texto refundido?",
        "option_a": "El artículo 24 regula la constitución de grupos políticos y el artículo 30 el Registro de Intereses",
        "option_b": "El artículo 24 regula presupuestos y el 30 elecciones generales",
        "option_c": "Ambos regulan exclusivamente sesiones plenarias",
        "option_d": "El artículo 24 regula tribunales y el 30 contratos estatales",
        "correct": "A",
        "explanation": "El artículo 24 establece requisitos de constitución de grupos políticos y el artículo 30 regula el Registro de Intereses de los miembros de la Corporación."
    }
])
# QUESTION_BANK_ACCEPTED_TOPIC_04_LOT_01_END

# QUESTION_BANK_ACCEPTED_TOPIC_05_LOT_01_START
SEED_QUESTIONS.extend([
    {
        "topic_num": 5,
        "question": "¿Qué regula principalmente la Ley 39/2015?",
        "option_a": "Los requisitos de validez y eficacia de los actos administrativos, el procedimiento común y los principios de iniciativa legislativa y potestad reglamentaria",
        "option_b": "La organización de los tribunales penales",
        "option_c": "Exclusivamente los contratos privados",
        "option_d": "Solo el régimen electoral",
        "correct": "A",
        "explanation": "El artículo 1 define el objeto de la Ley 39/2015 en esos términos, incluyendo el procedimiento administrativo común y la potestad sancionadora y de responsabilidad."
    },
    {
        "topic_num": 5,
        "question": "¿A qué entidades se aplica la Ley 39/2015 como Administraciones Públicas?",
        "option_a": "A la Administración General del Estado, Comunidades Autónomas, entidades locales y organismos públicos y entidades de derecho público vinculados o dependientes",
        "option_b": "Solo a la Administración General del Estado",
        "option_c": "Solo a sociedades mercantiles privadas",
        "option_d": "Únicamente a los órganos constitucionales",
        "correct": "A",
        "explanation": "El artículo 2.3 considera Administraciones Públicas la Administración General del Estado, las Administraciones autonómicas, las entidades locales y los organismos públicos y entidades de derecho público dependientes o vinculados."
    },
    {
        "topic_num": 5,
        "question": "¿Qué capacidad tienen los menores en sus relaciones con las Administraciones Públicas?",
        "option_a": "La capacidad de obrar que les reconozcan expresamente las leyes para el ejercicio y defensa de sus derechos e intereses, salvo limitación legal",
        "option_b": "Nunca pueden actuar sin autorización judicial",
        "option_c": "Tienen siempre plena capacidad administrativa",
        "option_d": "Solo pueden actuar como personas jurídicas",
        "correct": "A",
        "explanation": "El artículo 3 reconoce esa capacidad a los menores para el ejercicio y defensa de sus derechos e intereses cuya actuación permita el ordenamiento jurídico sin asistencia de quien ejerza patria potestad, tutela o curatela."
    },
    {
        "topic_num": 5,
        "question": "¿Quién tiene la condición de interesado en un procedimiento administrativo?",
        "option_a": "Quienes lo promuevan como titulares de derechos o intereses legítimos individuales o colectivos y quienes puedan resultar afectados por la resolución",
        "option_b": "Solo quien presente una denuncia penal",
        "option_c": "Únicamente los empleados públicos",
        "option_d": "Cualquier persona sin relación con el procedimiento",
        "correct": "A",
        "explanation": "El artículo 4.1 incluye a quienes promuevan el procedimiento y a quienes, sin haberlo iniciado, tengan derechos que puedan resultar afectados o intereses legítimos que puedan resultar afectados."
    },
    {
        "topic_num": 5,
        "question": "¿Qué ocurre con los sucesores en los derechos del interesado cuando este fallece?",
        "option_a": "Se subrogan en su posición cualquiera que sea el estado del procedimiento, salvo que la acción no sea transmisible",
        "option_b": "El procedimiento se archiva siempre",
        "option_c": "Solo pueden intervenir con autorización del Senado",
        "option_d": "Nunca pueden suceder al interesado",
        "correct": "A",
        "explanation": "El artículo 4.3 establece la sucesión en la posición del interesado cuando la condición derive de una relación transmisible, cualquiera que sea el estado del procedimiento."
    },
    {
        "topic_num": 5,
        "question": "¿Cuándo puede una persona actuar mediante representante ante la Administración?",
        "option_a": "Cuando tenga capacidad de obrar y, salvo manifestación expresa en contrario, las actuaciones se entienden con el representante",
        "option_b": "Solo en procedimientos sancionadores",
        "option_c": "Nunca en solicitudes o recursos",
        "option_d": "Solo si el representante es funcionario",
        "correct": "A",
        "explanation": "El artículo 5.1 permite actuar por medio de representante a los interesados con capacidad de obrar y dirige a este las actuaciones salvo manifestación expresa en contra."
    },
    {
        "topic_num": 5,
        "question": "¿Cómo puede acreditarse la representación?",
        "option_a": "Por cualquier medio válido en Derecho que deje constancia fidedigna de su existencia, incluido el apoderamiento apud acta",
        "option_b": "Solo mediante escritura pública",
        "option_c": "Solo mediante comparecencia presencial",
        "option_d": "No es necesario acreditarla para ningún trámite",
        "correct": "A",
        "explanation": "El artículo 5.4 admite cualquier medio válido en Derecho que deje constancia fidedigna y menciona el apud acta y el registro electrónico de apoderamientos."
    },
    {
        "topic_num": 5,
        "question": "Si falta o es insuficiente la acreditación de la representación, ¿qué debe hacer la Administración?",
        "option_a": "Conceder un plazo de diez días para aportar o subsanar, ampliable cuando las circunstancias lo requieran",
        "option_b": "Rechazar siempre el acto sin posibilidad de subsanación",
        "option_c": "Conceder un plazo de un año en todo caso",
        "option_d": "Remitir el expediente al Tribunal Constitucional",
        "correct": "A",
        "explanation": "El artículo 5.6 permite tener por realizado el acto si se aporta o subsana el defecto en diez días, o en un plazo superior si las circunstancias lo requieren."
    },
    {
        "topic_num": 5,
        "question": "¿Qué derecho tiene el interesado sobre el estado de su procedimiento?",
        "option_a": "A conocer en cualquier momento su tramitación, el sentido del silencio, el órgano competente y los actos de trámite, y a obtener copia de los documentos",
        "option_b": "Solo a conocerlo cuando termine",
        "option_c": "A consultar únicamente el presupuesto del órgano",
        "option_d": "No tiene derecho de información durante la tramitación",
        "correct": "A",
        "explanation": "El artículo 53.1.a reconoce esos derechos, incluido el acceso y copia de los documentos contenidos en el procedimiento."
    },
    {
        "topic_num": 5,
        "question": "¿Quiénes están obligados en todo caso a relacionarse electrónicamente con las Administraciones?",
        "option_a": "Las personas jurídicas, entre otros sujetos enumerados por la ley",
        "option_b": "Todas las personas físicas sin excepción",
        "option_c": "Solo quienes no tengan representante",
        "option_d": "Ningún interesado",
        "correct": "A",
        "explanation": "El artículo 14.2 incluye en todo caso a las personas jurídicas, entidades sin personalidad, determinados profesionales colegiados, representantes de obligados y empleados públicos en los supuestos previstos."
    },
    {
        "topic_num": 5,
        "question": "¿Puede una persona física cambiar el medio elegido para comunicarse con la Administración?",
        "option_a": "Sí, puede modificarlo en cualquier momento, salvo que esté obligada a relacionarse electrónicamente",
        "option_b": "No, la elección es irrevocable",
        "option_c": "Solo con autorización judicial",
        "option_d": "Solo una vez al año",
        "correct": "A",
        "explanation": "El artículo 14.1 permite a las personas físicas elegir el medio y modificarlo en cualquier momento, salvo obligación legal de relación electrónica."
    },
    {
        "topic_num": 5,
        "question": "¿Qué diferencia recoge la Ley 39/2015 entre identificación y firma electrónica?",
        "option_a": "La identificación permite verificar la identidad; la firma permite acreditar la voluntad y consentimiento, con los sistemas previstos legalmente",
        "option_b": "Son exactamente el mismo concepto y tienen siempre los mismos efectos",
        "option_c": "La firma solo identifica al órgano y nunca al interesado",
        "option_d": "La identificación solo puede hacerse en papel",
        "correct": "A",
        "explanation": "Los artículos 9 y 10 regulan sistemas de identificación y firma, con funciones jurídicas diferenciadas aunque puedan usar sistemas relacionados."
    },
    {
        "topic_num": 5,
        "question": "En un procedimiento de la Administración General del Estado en una Comunidad Autónoma con lengua cooficial, ¿qué regla lingüística se aplica?",
        "option_a": "El interesado puede usar también la lengua cooficial y el procedimiento se tramita en la lengua elegida, con las reglas legales para varios interesados",
        "option_b": "Solo puede usarse el castellano en todo caso",
        "option_c": "La Administración debe usar siempre cualquier lengua elegida por el primer interesado",
        "option_d": "La lengua depende del municipio, no de la ley",
        "correct": "A",
        "explanation": "El artículo 15.1 establece el castellano como lengua de la AGE, pero permite al interesado usar la lengua cooficial; si hay varios interesados con discrepancia, se tramita en castellano."
    },
    {
        "topic_num": 5,
        "question": "¿Qué documento no debe presentar el interesado, como regla general?",
        "option_a": "Datos y documentos no exigidos por la norma o que ya estén en poder de las Administraciones Públicas o hayan sido elaborados por ellas",
        "option_b": "Cualquier documento que funde su solicitud",
        "option_c": "El documento de identidad en todos los casos",
        "option_d": "Ningún documento en ningún procedimiento",
        "correct": "A",
        "explanation": "El artículo 53.1.d reconoce el derecho a no presentar datos y documentos no exigidos o que ya estén en poder de las Administraciones o hayan sido elaborados por ellas."
    },
    {
        "topic_num": 5,
        "question": "¿Hasta qué momento puede el interesado aportar documentos y alegaciones que deben tenerse en cuenta al redactar la propuesta?",
        "option_a": "En cualquier fase anterior al trámite de audiencia",
        "option_b": "Solo después de la resolución",
        "option_c": "Únicamente antes de iniciar el procedimiento",
        "option_d": "Solo durante la vía judicial",
        "correct": "A",
        "explanation": "El artículo 53.1.e reconoce ese derecho en cualquier fase del procedimiento anterior al trámite de audiencia."
    },
    {
        "topic_num": 5,
        "question": "¿Qué derecho de asistencia reconoce el artículo 53.1.g?",
        "option_a": "Actuar asistido de asesor cuando el interesado lo considere conveniente en defensa de sus intereses",
        "option_b": "Exigir siempre abogado de oficio administrativo",
        "option_c": "Ser representado obligatoriamente por un funcionario",
        "option_d": "Impedir toda actuación del órgano instructor",
        "correct": "A",
        "explanation": "El artículo 53.1.g reconoce al interesado el derecho a actuar asistido de asesor cuando lo considere conveniente en defensa de sus intereses."
    },
    {
        "topic_num": 5,
        "question": "¿A través de qué medios puede el interesado cumplir obligaciones de pago?",
        "option_a": "A través de los medios electrónicos previstos en el artículo 98.2",
        "option_b": "Solo mediante efectivo en la oficina del órgano",
        "option_c": "Solo por transferencia internacional",
        "option_d": "No puede hacerlo electrónicamente",
        "correct": "A",
        "explanation": "El artículo 53.1.h reconoce el derecho a cumplir obligaciones de pago mediante los medios electrónicos previstos en el artículo 98.2."
    },
    {
        "topic_num": 5,
        "question": "¿Puede una persona jurídica actuar como representante de otra ante una Administración?",
        "option_a": "Sí, cuando esté previsto en sus Estatutos, además de las personas físicas con capacidad de obrar",
        "option_b": "No, solo pueden representar los funcionarios",
        "option_c": "Sí, siempre sin necesidad de acreditación",
        "option_d": "Solo si la otra persona es una Administración",
        "correct": "A",
        "explanation": "El artículo 5.2 permite a las personas físicas con capacidad de obrar y a las personas jurídicas, cuando lo prevean sus Estatutos, actuar en representación de otras."
    },
    {
        "topic_num": 5,
        "question": "¿Qué ocurre si varios interesados discrepan sobre la lengua en un procedimiento de la AGE?",
        "option_a": "El procedimiento se tramita en castellano, aunque los documentos o testimonios se expiden en la lengua elegida por cada interesado",
        "option_b": "Se archiva el procedimiento",
        "option_c": "Decide siempre el primer interesado",
        "option_d": "Se tramita necesariamente en inglés",
        "correct": "A",
        "explanation": "El artículo 15.1 establece esa solución cuando concurren varios interesados y existe discrepancia sobre la lengua."
    },
    {
        "topic_num": 5,
        "question": "¿Qué afirmación diferencia correctamente actuar asistido de asesor y actuar mediante representante?",
        "option_a": "La asistencia de asesor es un derecho cuando conviene al interesado; la representación implica actuar por medio de otra persona conforme al artículo 5",
        "option_b": "Ambas figuras sustituyen siempre al interesado y exigen poder notarial",
        "option_c": "El asesor firma siempre en nombre del interesado",
        "option_d": "La representación solo existe en procedimientos judiciales",
        "correct": "A",
        "explanation": "El artículo 53.1.g reconoce asistencia de asesor, mientras que el artículo 5 regula la actuación mediante representante y sus efectos y acreditación."
    }
])
# QUESTION_BANK_ACCEPTED_TOPIC_05_LOT_01_END

# QUESTION_BANK_ACCEPTED_TOPIC_06_LOT_01_START
SEED_QUESTIONS.extend([
    {
        "topic_num": 6,
        "question": "¿Cuál es la regla general sobre los documentos que obran en los expedientes administrativos?",
        "option_a": "Se emitirán por escrito a través de medios electrónicos, salvo que su naturaleza exija otra forma más adecuada de expresión y constancia",
        "option_b": "Solo pueden emitirse en papel",
        "option_c": "Solo se admiten documentos notariales",
        "option_d": "Deben publicarse siempre en el BOE",
        "correct": "A",
        "explanation": "El artículo 26 establece la regla de emisión escrita por medios electrónicos, con la excepción ligada a la naturaleza del documento."
    },
    {
        "topic_num": 6,
        "question": "¿Qué debe contener un expediente administrativo?",
        "option_a": "El conjunto ordenado de documentos y actuaciones que sirven de antecedente y fundamento a la resolución, así como las diligencias encaminadas a ejecutarla",
        "option_b": "Solo la resolución final",
        "option_c": "Únicamente los escritos del interesado",
        "option_d": "Solo los documentos que el órgano considere favorables",
        "correct": "A",
        "explanation": "El artículo 70 define el expediente como un conjunto ordenado de documentos y actuaciones y exige incorporar la resolución y las diligencias de ejecución."
    },
    {
        "topic_num": 6,
        "question": "Cuando un plazo se señala por horas, ¿cómo se computa con carácter general?",
        "option_a": "De hora en hora y de minuto en minuto desde la hora y minuto en que tenga lugar la notificación o publicación del acto",
        "option_b": "Solo contando horas laborables",
        "option_c": "Por días completos desde las cero horas",
        "option_d": "Desde el siguiente lunes",
        "correct": "A",
        "explanation": "El artículo 30.1 dispone que los plazos expresados por horas se entienden hábiles y se computan de hora en hora y de minuto en minuto desde la notificación o publicación."
    },
    {
        "topic_num": 6,
        "question": "Si el último día de un plazo expresado en días es inhábil, ¿qué sucede?",
        "option_a": "Se prorroga al primer día hábil siguiente",
        "option_b": "Vence el día hábil anterior",
        "option_c": "Se duplica automáticamente",
        "option_d": "Debe reiniciarse todo el procedimiento",
        "correct": "A",
        "explanation": "El artículo 30.5 establece que cuando el último día sea inhábil se entenderá prorrogado al primer día hábil siguiente."
    },
    {
        "topic_num": 6,
        "question": "¿Cuándo puede concederse una ampliación de plazo?",
        "option_a": "Antes del vencimiento, de oficio o a petición, si las circunstancias lo aconsejan y no se perjudican derechos de tercero",
        "option_b": "Siempre después de vencido el plazo",
        "option_c": "Solo mediante sentencia judicial",
        "option_d": "Sin necesidad de motivación ni límite",
        "correct": "A",
        "explanation": "El artículo 32 exige que la ampliación se acuerde antes del vencimiento, cuando las circunstancias lo aconsejen y no se perjudiquen derechos de tercero."
    },
    {
        "topic_num": 6,
        "question": "¿Qué obligación general tiene la Administración al resolver un procedimiento?",
        "option_a": "Dictar resolución expresa y notificarla en todos los procedimientos, cualquiera que sea su forma de iniciación",
        "option_b": "Resolver solo los procedimientos iniciados de oficio",
        "option_c": "Resolver únicamente si lo pide el interesado",
        "option_d": "No resolver cuando opere el silencio",
        "correct": "A",
        "explanation": "El artículo 21 impone la obligación de dictar resolución expresa y notificarla en todos los procedimientos."
    },
    {
        "topic_num": 6,
        "question": "¿Qué efecto produce con carácter general el silencio en procedimientos iniciados a solicitud del interesado?",
        "option_a": "La estimación de la solicitud, salvo las excepciones legales",
        "option_b": "Siempre la desestimación",
        "option_c": "La nulidad del procedimiento",
        "option_d": "La suspensión indefinida",
        "correct": "A",
        "explanation": "El artículo 24 establece como regla general el silencio positivo, con las excepciones previstas por la ley o por norma con rango de ley."
    },
    {
        "topic_num": 6,
        "question": "¿Qué exige el artículo 34 para que un acto administrativo sea válido?",
        "option_a": "Que se dicte por el órgano competente y ajustándose a los requisitos y procedimiento establecidos",
        "option_b": "Que lo apruebe siempre un juez",
        "option_c": "Que se publique antes de dictarse",
        "option_d": "Que lo firme el interesado",
        "correct": "A",
        "explanation": "El artículo 34 exige que los actos se produzcan por el órgano competente y ajustándose a los requisitos y al procedimiento establecido."
    },
    {
        "topic_num": 6,
        "question": "¿Cuál de estos actos debe ser motivado?",
        "option_a": "El que limite derechos subjetivos o intereses legítimos",
        "option_b": "Todo acto de mero trámite sin excepción",
        "option_c": "Solo los actos favorables",
        "option_d": "Ningún acto administrativo",
        "correct": "A",
        "explanation": "El artículo 35 incluye entre los actos que deben motivarse los que limiten derechos subjetivos o intereses legítimos."
    },
    {
        "topic_num": 6,
        "question": "¿Cuál es la forma general de los actos administrativos?",
        "option_a": "Se producirán por escrito a través de medios electrónicos, salvo que su naturaleza exija otra forma más adecuada",
        "option_b": "Se dictarán siempre verbalmente",
        "option_c": "Se publicarán siempre antes de notificarse",
        "option_d": "Solo tendrán forma notarial",
        "correct": "A",
        "explanation": "El artículo 36 establece la forma escrita electrónica como regla general, con una excepción por la naturaleza del acto."
    },
    {
        "topic_num": 6,
        "question": "¿Cuándo producen efectos los actos administrativos?",
        "option_a": "Desde la fecha en que se dicten, salvo que se disponga otra cosa o su eficacia quede demorada por la propia naturaleza del acto",
        "option_b": "Solo desde su publicación en el BOE",
        "option_c": "Siempre desde un mes después",
        "option_d": "Solo cuando los acepte el interesado",
        "correct": "A",
        "explanation": "El artículo 39.1 fija la eficacia desde la fecha en que se dictan, salvo disposición en contrario o demora legalmente prevista."
    },
    {
        "topic_num": 6,
        "question": "¿En qué plazo debe cursarse una notificación desde que se dicta el acto?",
        "option_a": "Dentro del plazo de diez días desde que se dictó el acto",
        "option_b": "Dentro de tres meses en todo caso",
        "option_c": "Solo al finalizar el año",
        "option_d": "No existe plazo legal",
        "correct": "A",
        "explanation": "El artículo 40.2 indica que toda notificación debe cursarse dentro del plazo de diez días a partir de la fecha en que el acto haya sido dictado."
    },
    {
        "topic_num": 6,
        "question": "¿Qué debe incluir la notificación de una resolución?",
        "option_a": "El texto íntegro de la resolución, si pone fin o no a la vía administrativa, los recursos procedentes, el órgano ante el que interponerlos y el plazo",
        "option_b": "Solo la parte dispositiva",
        "option_c": "Únicamente el plazo para recurrir",
        "option_d": "Solo una referencia al número de expediente",
        "correct": "A",
        "explanation": "El artículo 40.2 exige el texto íntegro y la indicación de los recursos, órgano y plazo, entre otros extremos."
    },
    {
        "topic_num": 6,
        "question": "¿Cuándo puede la publicación sustituir a la notificación?",
        "option_a": "Cuando el acto tenga por destinatarios una pluralidad indeterminada o cuando la Administración estime que la notificación a un solo interesado es insuficiente para garantizar la notificación a todos",
        "option_b": "Siempre que el órgano prefiera publicar",
        "option_c": "Solo en actos favorables",
        "option_d": "Nunca",
        "correct": "A",
        "explanation": "El artículo 45 prevé esos supuestos de publicación sustitutiva o complementaria de la notificación."
    },
    {
        "topic_num": 6,
        "question": "¿Cuál es causa de nulidad de pleno derecho?",
        "option_a": "Un acto que lesione los derechos y libertades susceptibles de amparo constitucional",
        "option_b": "Cualquier error material corregible",
        "option_c": "Toda infracción de un plazo no esencial",
        "option_d": "Cualquier acto desfavorable",
        "correct": "A",
        "explanation": "El artículo 47.1.a declara nulos los actos que lesionen los derechos y libertades susceptibles de amparo constitucional."
    },
    {
        "topic_num": 6,
        "question": "¿Qué caracteriza a la anulabilidad?",
        "option_a": "Cualquier infracción del ordenamiento jurídico, incluida la desviación de poder, salvo los supuestos de nulidad de pleno derecho",
        "option_b": "Solo la lesión de derechos fundamentales",
        "option_c": "La inexistencia absoluta del acto",
        "option_d": "La imposibilidad de impugnación",
        "correct": "A",
        "explanation": "El artículo 48.1 establece la anulabilidad para las infracciones del ordenamiento jurídico, incluida la desviación de poder, fuera de los casos de nulidad."
    },
    {
        "topic_num": 6,
        "question": "¿Qué efecto tiene la conservación de actos y trámites?",
        "option_a": "El órgano que resuelve la nulidad o anulación puede disponer la conservación de actos y trámites cuyo contenido se habría mantenido igual",
        "option_b": "Obliga a repetir siempre todo el procedimiento",
        "option_c": "Convierte automáticamente todo acto nulo en válido",
        "option_d": "Impide subsanar cualquier defecto",
        "correct": "A",
        "explanation": "El artículo 51 permite conservar aquellos actos y trámites cuyo contenido se hubiera mantenido igual de no haberse cometido la infracción."
    },
    {
        "topic_num": 6,
        "question": "¿Qué debe hacer la Administración para impugnar ante la jurisdicción un acto favorable que considera lesivo para el interés público?",
        "option_a": "Declarar previamente su lesividad para el interés público",
        "option_b": "Anularlo directamente sin procedimiento",
        "option_c": "Solicitar autorización del interesado",
        "option_d": "Publicarlo sin más trámite",
        "correct": "A",
        "explanation": "El artículo 107 exige la previa declaración de lesividad para impugnar actos favorables que sean anulables."
    },
    {
        "topic_num": 6,
        "question": "¿Cuándo puede ampliarse el plazo máximo para resolver y notificar?",
        "option_a": "Excepcionalmente, cuando se hayan agotado los medios personales y materiales disponibles, y con motivación",
        "option_b": "Siempre que el órgano esté ocupado",
        "option_c": "Después de vencido el plazo sin resolución",
        "option_d": "Sin resolución expresa de ampliación",
        "correct": "A",
        "explanation": "El artículo 23 permite ampliar excepcionalmente el plazo máximo cuando se han agotado los medios disponibles, mediante resolución motivada."
    },
    {
        "topic_num": 6,
        "question": "¿Cuándo se entiende rechazada una notificación electrónica obligatoria o elegida que no se abre?",
        "option_a": "Cuando transcurren diez días naturales desde su puesta a disposición sin acceder a su contenido",
        "option_b": "Cuando transcurren diez días hábiles desde la firma del acto",
        "option_c": "Al día siguiente de enviarse siempre",
        "option_d": "Nunca se entiende rechazada",
        "correct": "A",
        "explanation": "El artículo 43.2 establece el rechazo transcurridos diez días naturales desde la puesta a disposición sin acceso, salvo imposibilidad técnica o material justificada."
    }
])
# QUESTION_BANK_ACCEPTED_TOPIC_06_LOT_01_END

# QUESTION_BANK_ACCEPTED_TOPIC_07_LOT_01_START
SEED_QUESTIONS.extend([
    {
        "topic_num": 7,
        "question": "¿Qué es la prevención según la Ley 31/1995?",
        "option_a": "El conjunto de actividades o medidas adoptadas o previstas en todas las fases de actividad para evitar o disminuir los riesgos derivados del trabajo",
        "option_b": "La reparación económica posterior al accidente",
        "option_c": "Solo la entrega de equipos de protección",
        "option_d": "La vigilancia médica anual exclusivamente",
        "correct": "A",
        "explanation": "El artículo 4.1 define la prevención como el conjunto de actividades o medidas adoptadas o previstas en todas las fases de actividad para evitar o disminuir los riesgos derivados del trabajo."
    },
    {
        "topic_num": 7,
        "question": "¿Cuál es el objeto de la Ley de Prevención de Riesgos Laborales?",
        "option_a": "Promover la seguridad y la salud de los trabajadores mediante medidas y actividades preventivas",
        "option_b": "Regular exclusivamente las pensiones",
        "option_c": "Sustituir toda negociación colectiva",
        "option_d": "Regular solo los accidentes ya producidos",
        "correct": "A",
        "explanation": "La ley tiene por objeto promover la seguridad y la salud de los trabajadores mediante la aplicación de medidas y actividades preventivas."
    },
    {
        "topic_num": 7,
        "question": "¿Qué derecho reconoce el artículo 14 a los trabajadores?",
        "option_a": "Una protección eficaz en materia de seguridad y salud en el trabajo",
        "option_b": "Elegir siempre el equipo directivo",
        "option_c": "No recibir ninguna instrucción preventiva",
        "option_d": "Renunciar por contrato a toda protección",
        "correct": "A",
        "explanation": "El artículo 14 reconoce el derecho de los trabajadores a una protección eficaz en materia de seguridad y salud en el trabajo."
    },
    {
        "topic_num": 7,
        "question": "¿Quién debe garantizar la seguridad y salud de los trabajadores?",
        "option_a": "El empresario, en todos los aspectos relacionados con el trabajo",
        "option_b": "Solo el servicio de prevención externo",
        "option_c": "El trabajador individualmente",
        "option_d": "La inspección de trabajo en lugar del empresario",
        "correct": "A",
        "explanation": "El artículo 14.2 atribuye al empresario el deber de garantizar la seguridad y salud de los trabajadores a su servicio en todos los aspectos relacionados con el trabajo."
    },
    {
        "topic_num": 7,
        "question": "¿Puede el empresario trasladar su responsabilidad preventiva al trabajador?",
        "option_a": "No; la atribución de funciones preventivas a trabajadores o servicios no exime al empresario de su deber",
        "option_b": "Sí, mediante una cláusula contractual",
        "option_c": "Sí, si el trabajador recibe formación",
        "option_d": "Solo cuando existe servicio de prevención",
        "correct": "A",
        "explanation": "El artículo 14.4 dispone que las obligaciones de los trabajadores y las funciones atribuidas a otras personas no eximen al empresario de su responsabilidad."
    },
    {
        "topic_num": 7,
        "question": "¿Cuál es un principio de la acción preventiva?",
        "option_a": "Evitar los riesgos y evaluar los que no se puedan evitar",
        "option_b": "Aumentar siempre la exposición para medirla",
        "option_c": "Priorizar la protección individual sobre la colectiva en todo caso",
        "option_d": "Esperar al accidente antes de actuar",
        "correct": "A",
        "explanation": "El artículo 15 incluye evitar los riesgos, evaluar los inevitables y combatirlos en su origen, entre otros principios."
    },
    {
        "topic_num": 7,
        "question": "¿Cómo debe integrarse la prevención en la empresa?",
        "option_a": "En el sistema general de gestión de la empresa, mediante un plan de prevención",
        "option_b": "Como una actividad separada de toda decisión de gestión",
        "option_c": "Solo en el departamento de recursos humanos",
        "option_d": "Únicamente después de una inspección",
        "correct": "A",
        "explanation": "El artículo 16 exige integrar la prevención en el sistema general de gestión mediante el plan de prevención."
    },
    {
        "topic_num": 7,
        "question": "¿Cuándo debe utilizarse protección individual?",
        "option_a": "Cuando los riesgos no se puedan evitar o limitar suficientemente por medios de protección colectiva o procedimientos de organización del trabajo",
        "option_b": "Siempre antes de evaluar riesgos",
        "option_c": "Solo si el trabajador la compra",
        "option_d": "Nunca si existe formación",
        "correct": "A",
        "explanation": "El artículo 17.2 exige proporcionar equipos de protección individual cuando los riesgos no puedan evitarse o limitarse suficientemente por protección colectiva u organización."
    },
    {
        "topic_num": 7,
        "question": "¿Qué debe hacer el empresario respecto de la información preventiva?",
        "option_a": "Informar sobre los riesgos para la seguridad y salud y sobre las medidas y actividades de protección y prevención aplicables",
        "option_b": "Informar solo después del accidente",
        "option_c": "No informar si existe un manual general",
        "option_d": "Informar únicamente a los representantes",
        "correct": "A",
        "explanation": "El artículo 18 exige información sobre riesgos, medidas y actividades de protección y prevención y medidas de emergencia."
    },
    {
        "topic_num": 7,
        "question": "¿Qué características debe tener la formación preventiva?",
        "option_a": "Ser suficiente y adecuada, teórica y práctica, al contratar y cuando cambien funciones o tecnologías",
        "option_b": "Ser siempre voluntaria y solo teórica",
        "option_c": "Darse únicamente al personal directivo",
        "option_d": "Darse solo una vez en toda la vida laboral",
        "correct": "A",
        "explanation": "El artículo 19 exige formación suficiente y adecuada, teórica y práctica, tanto al inicio como cuando cambien funciones, tecnologías o equipos."
    },
    {
        "topic_num": 7,
        "question": "¿Qué debe prever el empresario en materia de emergencias?",
        "option_a": "Medidas de primeros auxilios, lucha contra incendios y evacuación, designando personal y comprobando periódicamente su funcionamiento",
        "option_b": "Solo un teléfono de emergencias",
        "option_c": "Únicamente un seguro de accidentes",
        "option_d": "La evacuación sin personal designado",
        "correct": "A",
        "explanation": "El artículo 20 exige analizar posibles emergencias y adoptar medidas de primeros auxilios, lucha contra incendios y evacuación."
    },
    {
        "topic_num": 7,
        "question": "Ante un riesgo grave e inminente, ¿qué derecho tiene el trabajador?",
        "option_a": "Interrumpir su actividad y abandonar el lugar si resulta necesario, en los términos legales",
        "option_b": "Continuar siempre aunque exista peligro",
        "option_c": "Despedir al responsable preventivo",
        "option_d": "Imponer una sanción penal",
        "correct": "A",
        "explanation": "El artículo 21 reconoce el derecho a interrumpir la actividad y abandonar el lugar cuando sea necesario ante un riesgo grave e inminente."
    },
    {
        "topic_num": 7,
        "question": "¿Cuál es la regla general sobre vigilancia de la salud?",
        "option_a": "Requiere el consentimiento del trabajador, salvo las excepciones previstas legalmente",
        "option_b": "Es obligatoria sin excepción",
        "option_c": "Solo puede hacerla la Inspección de Trabajo",
        "option_d": "No puede realizarse nunca",
        "correct": "A",
        "explanation": "El artículo 22 establece que la vigilancia periódica de la salud requiere el consentimiento del trabajador, con excepciones vinculadas a riesgos concretos y garantías legales."
    },
    {
        "topic_num": 7,
        "question": "¿Qué documento debe incluir el empresario en materia preventiva?",
        "option_a": "La evaluación de riesgos y la planificación de la actividad preventiva, incluida la protección y prevención y los equipos de protección",
        "option_b": "Solo el registro salarial",
        "option_c": "Únicamente el calendario laboral",
        "option_d": "Solo partes de accidentes ya ocurridos",
        "correct": "A",
        "explanation": "El artículo 23 exige documentación preventiva, entre ella la evaluación de riesgos y la planificación de la actividad preventiva."
    },
    {
        "topic_num": 7,
        "question": "Cuando varias empresas trabajan en un mismo centro, ¿qué deben hacer?",
        "option_a": "Cooperar en la aplicación de la normativa preventiva y establecer los medios de coordinación necesarios",
        "option_b": "Actuar sin comunicarse",
        "option_c": "Transferir toda responsabilidad a la empresa principal siempre",
        "option_d": "Coordinarse solo después de un accidente",
        "correct": "A",
        "explanation": "El artículo 24 exige cooperación y coordinación cuando concurren trabajadores de varias empresas en un mismo centro de trabajo."
    },
    {
        "topic_num": 7,
        "question": "¿Qué debe hacer el empresario respecto de trabajadores especialmente sensibles?",
        "option_a": "Garantizar una protección específica y no emplearlos en puestos incompatibles con sus características conocidas",
        "option_b": "Asignarles siempre los puestos de mayor riesgo",
        "option_c": "Excluirlos de toda formación",
        "option_d": "No tenerlos en cuenta si aceptan el puesto",
        "correct": "A",
        "explanation": "El artículo 25 exige protección específica de trabajadores especialmente sensibles y prohíbe emplearlos en puestos incompatibles con sus características."
    },
    {
        "topic_num": 7,
        "question": "Si la evaluación revela riesgo para una trabajadora embarazada, ¿qué debe intentarse primero?",
        "option_a": "Adaptar las condiciones o el tiempo de trabajo y, si no es posible, cambiar de puesto o aplicar las medidas previstas legalmente",
        "option_b": "Despedirla automáticamente",
        "option_c": "Eliminar toda vigilancia de la salud",
        "option_d": "Mantener siempre el puesto sin cambios",
        "correct": "A",
        "explanation": "El artículo 26 establece una secuencia de adaptación y cambio de puesto, con la protección específica durante embarazo y lactancia."
    },
    {
        "topic_num": 7,
        "question": "¿Qué obligación preventiva tiene cada trabajador?",
        "option_a": "Velar por su propia seguridad y salud y por la de otras personas afectadas por su actividad, conforme a su formación e instrucciones",
        "option_b": "Diseñar la política preventiva de la empresa",
        "option_c": "Sustituir al empresario en toda obligación",
        "option_d": "No usar los equipos proporcionados",
        "correct": "A",
        "explanation": "El artículo 29 obliga a cada trabajador a velar por su seguridad y la de otras personas, usando adecuadamente máquinas, equipos y dispositivos."
    },
    {
        "topic_num": 7,
        "question": "¿Cómo participan los trabajadores en la prevención?",
        "option_a": "A través de los Delegados de Prevención y del Comité de Seguridad y Salud en los supuestos legales",
        "option_b": "Solo mediante el comité de empresa estatal",
        "option_c": "Únicamente mediante denuncias judiciales",
        "option_d": "No participan en la prevención",
        "correct": "A",
        "explanation": "Los artículos 34 y 35 regulan los derechos de participación y representación mediante Delegados de Prevención y otros órganos."
    },
    {
        "topic_num": 7,
        "question": "¿Qué función tiene un servicio de prevención?",
        "option_a": "Proporcionar asesoramiento y apoyo para diseñar y aplicar la acción preventiva, sin sustituir el deber general del empresario",
        "option_b": "Asumir siempre toda responsabilidad empresarial",
        "option_c": "Representar judicialmente a todos los trabajadores",
        "option_d": "Realizar únicamente reconocimientos médicos",
        "correct": "A",
        "explanation": "El artículo 31 configura los servicios de prevención como medios de asesoramiento y apoyo para la actividad preventiva y no como sustitutos del deber empresarial."
    }
])
# QUESTION_BANK_ACCEPTED_TOPIC_07_LOT_01_END

# QUESTION_BANK_ACCEPTED_TOPIC_08_LOT_01_START
SEED_QUESTIONS.extend([
    {
        "topic_num": 8,
        "question": "¿Cuál es el objeto de la Ley Orgánica 3/2007?",
        "option_a": "Hacer efectivo el derecho de igualdad de trato y de oportunidades entre mujeres y hombres, especialmente mediante la eliminación de la discriminación de la mujer",
        "option_b": "Regular exclusivamente la igualdad tributaria",
        "option_c": "Sustituir el derecho laboral",
        "option_d": "Regular solo las elecciones",
        "correct": "A",
        "explanation": "El artículo 1 establece el objeto de hacer efectivo el derecho de igualdad de trato y oportunidades y eliminar la discriminación de la mujer."
    },
    {
        "topic_num": 8,
        "question": "¿Qué es discriminación directa por razón de sexo?",
        "option_a": "La situación en que una persona es, ha sido o pudiera ser tratada de manera menos favorable que otra en situación comparable por razón de sexo",
        "option_b": "Una medida general siempre favorable",
        "option_c": "Una diferencia basada solo en antigüedad",
        "option_d": "La ausencia de cualquier comparación",
        "correct": "A",
        "explanation": "El artículo 6.1 define la discriminación directa en esos términos."
    },
    {
        "topic_num": 8,
        "question": "¿Qué conducta constituye acoso sexual?",
        "option_a": "Cualquier comportamiento, verbal o físico, de naturaleza sexual que tenga el propósito o produzca el efecto de atentar contra la dignidad y crear un entorno intimidatorio, degradante u ofensivo",
        "option_b": "Solo una agresión física con sentencia penal",
        "option_c": "Cualquier crítica profesional",
        "option_d": "Una diferencia salarial objetiva",
        "correct": "A",
        "explanation": "El artículo 7.1 define el acoso sexual como comportamiento de naturaleza sexual con ese propósito o efecto."
    },
    {
        "topic_num": 8,
        "question": "¿Qué es acoso por razón de sexo?",
        "option_a": "Un comportamiento realizado en función del sexo de una persona que atenta contra su dignidad y crea un entorno intimidatorio, degradante u ofensivo",
        "option_b": "Toda diferencia de trato favorable",
        "option_c": "Solo una conducta fuera del trabajo",
        "option_d": "Una medida de acción positiva",
        "correct": "A",
        "explanation": "El artículo 7.2 define el acoso por razón de sexo en esos términos."
    },
    {
        "topic_num": 8,
        "question": "¿Qué efecto tiene una orden de discriminar por razón de sexo?",
        "option_a": "También constituye discriminación por razón de sexo",
        "option_b": "No tiene relevancia jurídica",
        "option_c": "Solo es discriminatoria si se ejecuta físicamente",
        "option_d": "Es siempre una acción positiva",
        "correct": "A",
        "explanation": "El artículo 6.3 dispone que se considera discriminación toda orden de discriminar, directa o indirectamente, por razón de sexo."
    },
    {
        "topic_num": 8,
        "question": "¿Qué son las acciones positivas?",
        "option_a": "Medidas específicas a favor de las mujeres para corregir situaciones patentes de desigualdad de hecho respecto de los hombres",
        "option_b": "Medidas que siempre perjudican a los hombres",
        "option_c": "Sanciones penales automáticas",
        "option_d": "Medidas aplicables solo por tribunales",
        "correct": "A",
        "explanation": "El artículo 11 permite medidas específicas a favor de las mujeres para corregir desigualdades de hecho, razonables y proporcionadas."
    },
    {
        "topic_num": 8,
        "question": "¿Qué principio se aplica a las condiciones de trabajo?",
        "option_a": "El principio de igualdad de trato y de oportunidades debe garantizarse en el empleo privado y público",
        "option_b": "Solo se aplica al acceso inicial",
        "option_c": "Solo se aplica a contratos indefinidos",
        "option_d": "No se aplica a la promoción",
        "correct": "A",
        "explanation": "El artículo 5 extiende la igualdad de trato y oportunidades al empleo, la formación, la promoción profesional y las condiciones de trabajo."
    },
    {
        "topic_num": 8,
        "question": "¿Qué debe contener un plan de igualdad?",
        "option_a": "Un conjunto ordenado de medidas evaluables para hacer efectiva la igualdad y evitar cualquier discriminación por razón de sexo",
        "option_b": "Solo una declaración de intenciones",
        "option_c": "Únicamente un calendario de vacaciones",
        "option_d": "Una relación de sanciones penales",
        "correct": "A",
        "explanation": "Los artículos 45 y 46 configuran los planes de igualdad como medidas ordenadas y evaluables tras un diagnóstico de situación."
    },
    {
        "topic_num": 8,
        "question": "¿Qué promueve la Ley Orgánica 3/2007 en la negociación colectiva?",
        "option_a": "La adopción de medidas dirigidas a evitar cualquier tipo de discriminación laboral entre mujeres y hombres y, en su caso, planes de igualdad",
        "option_b": "La exclusión de la igualdad de los convenios",
        "option_c": "Solo la negociación salarial masculina",
        "option_d": "La prohibición de toda negociación",
        "correct": "A",
        "explanation": "El artículo 43 promueve medidas de acción positiva mediante negociación colectiva para favorecer la igualdad real."
    },
    {
        "topic_num": 8,
        "question": "¿Qué regla probatoria se aplica en procedimientos por discriminación?",
        "option_a": "La persona demandada debe probar la ausencia de discriminación en los términos previstos, salvo en procesos penales",
        "option_b": "La persona discriminada debe probar siempre todos los hechos y la intención",
        "option_c": "Nunca se admite prueba estadística",
        "option_d": "La carga corresponde siempre al juez",
        "correct": "A",
        "explanation": "El artículo 13 prevé la inversión de la carga de la prueba en los procesos civiles, laborales y contencioso-administrativos, con la excepción de los procesos penales."
    },
    {
        "topic_num": 8,
        "question": "¿Qué protección tiene una persona frente a una discriminación por razón de sexo?",
        "option_a": "Puede recabar tutela judicial y reclamar indemnización o reparación efectiva, proporcional y disuasoria",
        "option_b": "Solo puede presentar una queja interna",
        "option_c": "No puede reclamar daños",
        "option_d": "Solo puede acudir a la vía penal",
        "correct": "A",
        "explanation": "El artículo 12 reconoce tutela judicial efectiva y el artículo 10 establece consecuencias jurídicas y reparación para conductas discriminatorias."
    },
    {
        "topic_num": 8,
        "question": "¿Qué deben promover las Administraciones Públicas en el acceso al empleo público?",
        "option_a": "La presencia equilibrada de mujeres y hombres y la igualdad en el acceso, formación, promoción y condiciones de trabajo",
        "option_b": "La selección de un solo sexo",
        "option_c": "La eliminación de los méritos",
        "option_d": "La promoción sin procedimiento",
        "correct": "A",
        "explanation": "El artículo 51 enumera criterios de actuación de las Administraciones Públicas para hacer efectivo el principio de igualdad en el empleo público."
    },
    {
        "topic_num": 8,
        "question": "¿Qué puede incluirse en contratos y subvenciones públicas para promover la igualdad?",
        "option_a": "Condiciones especiales relacionadas con la igualdad y medidas de igualdad en los contratos y subvenciones, dentro de la legislación aplicable",
        "option_b": "Solo criterios de antigüedad",
        "option_c": "La prohibición de contratar con empresas privadas",
        "option_d": "Ninguna condición social",
        "correct": "A",
        "explanation": "Los artículos 33 y 35 permiten establecer condiciones especiales y criterios relacionados con la igualdad en contratos y subvenciones públicas."
    },
    {
        "topic_num": 8,
        "question": "¿Qué debe preceder a la elaboración de medidas de un plan de igualdad?",
        "option_a": "Un diagnóstico de situación negociado o elaborado conforme a la normativa aplicable",
        "option_b": "Una sentencia penal",
        "option_c": "La supresión de la representación legal",
        "option_d": "La aprobación sin análisis",
        "correct": "A",
        "explanation": "El artículo 46 vincula el contenido del plan de igualdad al diagnóstico de situación y a las materias legalmente previstas."
    },
    {
        "topic_num": 8,
        "question": "¿Qué conducta constituye discriminación directa por razón de sexo en relación con el embarazo?",
        "option_a": "Todo trato desfavorable a las mujeres relacionado con el embarazo o la maternidad",
        "option_b": "Solo el despido declarado por un juez",
        "option_c": "Ningún trato vinculado a la maternidad",
        "option_d": "Solo la diferencia salarial pactada",
        "correct": "A",
        "explanation": "El artículo 8 considera discriminación directa por razón de sexo todo trato desfavorable a las mujeres relacionado con el embarazo o la maternidad."
    },
    {
        "topic_num": 8,
        "question": "¿Qué es la indemnidad frente a represalias?",
        "option_a": "La protección frente a trato adverso o efecto negativo por presentar queja, reclamación o denuncia destinada a impedir discriminación",
        "option_b": "La inmunidad penal de cualquier empleado",
        "option_c": "La obligación de ocultar la denuncia",
        "option_d": "La prohibición de investigar",
        "correct": "A",
        "explanation": "El artículo 9 protege frente a represalias por presentar queja, reclamación, denuncia o recurso para impedir la discriminación."
    },
    {
        "topic_num": 8,
        "question": "¿Qué deben evitar los poderes públicos en sus comunicaciones?",
        "option_a": "El lenguaje sexista y los estereotipos discriminatorios, promoviendo una imagen igualitaria y plural",
        "option_b": "Toda referencia a mujeres y hombres",
        "option_c": "La información sobre igualdad",
        "option_d": "El uso de lenguaje claro",
        "correct": "A",
        "explanation": "El artículo 14 incluye la implantación de un lenguaje no sexista en el ámbito administrativo y su fomento en las relaciones sociales."
    },
    {
        "topic_num": 8,
        "question": "¿Qué objetivo tiene la igualdad en la formación profesional?",
        "option_a": "Garantizar una formación que permita el desarrollo de la carrera profesional sin discriminación y con igualdad de oportunidades",
        "option_b": "Reservar la formación a un sexo",
        "option_c": "Eliminar la formación continua",
        "option_d": "Limitar la orientación profesional",
        "correct": "A",
        "explanation": "El Título IV incorpora medidas de igualdad en la formación profesional y el acceso y permanencia en el empleo."
    },
    {
        "topic_num": 8,
        "question": "¿Qué obligación tiene la publicidad institucional respecto de la igualdad?",
        "option_a": "No puede justificar o tolerar la discriminación por razón de sexo y debe respetar la igualdad",
        "option_b": "Puede usar estereotipos si vende un producto",
        "option_c": "Solo debe respetar la igualdad en campañas electorales",
        "option_d": "No está sujeta a ninguna regla",
        "correct": "A",
        "explanation": "La ley contiene criterios de actuación de los poderes públicos y prohíbe la publicidad o comunicación que comporte discriminación por razón de sexo."
    },
    {
        "topic_num": 8,
        "question": "¿Qué implica la transversalidad del principio de igualdad?",
        "option_a": "Integrar activamente la igualdad de trato y oportunidades en la elaboración y aplicación de todas las políticas públicas",
        "option_b": "Aplicarla solo en políticas sociales",
        "option_c": "Aplicarla únicamente después de una denuncia",
        "option_d": "Sustituir todas las políticas sectoriales",
        "correct": "A",
        "explanation": "El artículo 15 exige integrar de forma activa el principio de igualdad en la elaboración y ejecución de las disposiciones normativas y políticas públicas."
    }
])
# QUESTION_BANK_ACCEPTED_TOPIC_08_LOT_01_END

# QUESTION_BANK_ACCEPTED_TOPIC_09_LOT_01_START
SEED_QUESTIONS.extend([
    {
        "topic_num": 9,
        "question": "¿Qué relación describe correctamente la identificación electrónica y la firma electrónica?",
        "option_a": "La identificación acredita quién es una persona o entidad; la firma se vincula a datos firmados y expresa o acredita voluntad",
        "option_b": "Son siempre idénticas",
        "option_c": "La firma solo sirve para cifrar",
        "option_d": "La identificación solo existe en papel",
        "correct": "A",
        "explanation": "El eIDAS define identificación electrónica y firma como conceptos relacionados pero distintos, con funciones propias."
    },
    {
        "topic_num": 9,
        "question": "¿Qué principio establece eIDAS para no obstaculizar el mercado interior?",
        "option_a": "No se denegarán efectos jurídicos ni admisibilidad como prueba a una firma electrónica por el mero hecho de ser electrónica o no cualificada",
        "option_b": "Solo las firmas cualificadas tienen cualquier efecto",
        "option_c": "Las firmas electrónicas son inválidas fuera del país de emisión",
        "option_d": "La firma electrónica sustituye siempre a la identificación",
        "correct": "A",
        "explanation": "El artículo 25.1 contiene la regla de que no se denieguen efectos jurídicos ni admisibilidad probatoria por la forma electrónica o por no ser cualificada."
    },
    {
        "topic_num": 9,
        "question": "¿Qué exige eIDAS a los Estados miembros respecto de ciertos medios de identificación electrónica notificados?",
        "option_a": "Reconocer los medios de identificación electrónica de otros Estados miembros en las condiciones del Reglamento",
        "option_b": "Reconocer cualquier contraseña privada",
        "option_c": "No reconocer ningún medio extranjero",
        "option_d": "Reconocer solo documentos en papel",
        "correct": "A",
        "explanation": "El artículo 6 regula el reconocimiento mutuo de medios de identificación electrónica notificados en el nivel de seguridad correspondiente."
    },
    {
        "topic_num": 9,
        "question": "¿Qué es un servicio de confianza?",
        "option_a": "Un servicio electrónico consistente en creación, verificación y validación de firmas, sellos, sellos de tiempo, entrega certificada u otros servicios definidos por eIDAS",
        "option_b": "Cualquier red social",
        "option_c": "Solo un certificado de papel",
        "option_d": "Un sistema de copias de seguridad",
        "correct": "A",
        "explanation": "El artículo 3 enumera los servicios electrónicos de confianza y sus categorías."
    },
    {
        "topic_num": 9,
        "question": "¿Qué distingue una firma electrónica avanzada?",
        "option_a": "Está vinculada de forma única al firmante, permite identificarlo, se crea con datos bajo su control y detecta cambios posteriores en los datos firmados",
        "option_b": "Solo contiene una imagen escaneada",
        "option_c": "No se vincula al firmante",
        "option_d": "Es necesariamente un sello de empresa",
        "correct": "A",
        "explanation": "El artículo 26 establece los requisitos acumulativos de una firma electrónica avanzada."
    },
    {
        "topic_num": 9,
        "question": "¿Qué efecto tiene una firma electrónica cualificada?",
        "option_a": "Tiene un efecto jurídico equivalente al de una firma manuscrita",
        "option_b": "No tiene valor probatorio",
        "option_c": "Solo sirve para cifrar mensajes",
        "option_d": "Es válida únicamente dentro de la empresa",
        "correct": "A",
        "explanation": "El artículo 25.2 reconoce a la firma electrónica cualificada un efecto jurídico equivalente al de la firma manuscrita."
    },
    {
        "topic_num": 9,
        "question": "¿Qué acredita un certificado cualificado de firma electrónica?",
        "option_a": "La vinculación de los datos de validación de una firma con una persona física y la identidad de esta conforme a los requisitos cualificados",
        "option_b": "La identidad de cualquier servidor web sin firmante",
        "option_c": "Solo la fecha de emisión",
        "option_d": "La existencia de una contraseña",
        "correct": "A",
        "explanation": "El régimen de certificados cualificados y sus requisitos se regula en los artículos 28 y 3 del Reglamento."
    },
    {
        "topic_num": 9,
        "question": "¿Qué debe garantizar un dispositivo cualificado de creación de firma?",
        "option_a": "Que los datos de creación de firma permanezcan confidenciales, sean únicos y estén protegidos frente a falsificación y uso ajeno",
        "option_b": "Que comparta la clave privada públicamente",
        "option_c": "Que impida toda verificación",
        "option_d": "Que solo almacene documentos en papel",
        "correct": "A",
        "explanation": "El artículo 29 y el anexo II fijan requisitos de los dispositivos cualificados de creación de firma."
    },
    {
        "topic_num": 9,
        "question": "¿Qué es AutoFirma según su fuente oficial de descargas?",
        "option_a": "Una aplicación cliente que se descarga desde el portal oficial de firma electrónica para realizar operaciones de firma electrónica",
        "option_b": "Un prestador cualificado por sí mismo",
        "option_c": "Un protocolo de transporte",
        "option_d": "Un certificado raíz europeo",
        "correct": "A",
        "explanation": "La página oficial de descargas de firma electrónica identifica AutoFirma como aplicación cliente de firma; la página no autoriza a atribuirle la condición de prestador cualificado."
    },
    {
        "topic_num": 9,
        "question": "¿Qué debe hacer un lote que formule una pregunta sobre la versión concreta de AutoFirma?",
        "option_a": "Fijar y registrar la versión descargada y su fecha de verificación",
        "option_b": "Usar siempre la última versión sin anotarla",
        "option_c": "Atribuirle la versión al Reglamento eIDAS",
        "option_d": "No registrar la fuente",
        "correct": "A",
        "explanation": "El registro de fuente indica que la versión de la aplicación debe fijarse por lote; una pregunta version-sensitive no puede dejar la versión implícita."
    },
    {
        "topic_num": 9,
        "question": "¿Qué función cumple una aplicación cliente como AutoFirma en un flujo de firma?",
        "option_a": "Ejecuta localmente la operación de firma con los medios del firmante, pero no se convierte por ello en el prestador del servicio de confianza",
        "option_b": "Emite siempre certificados cualificados",
        "option_c": "Sustituye al organismo que recibe el documento",
        "option_d": "Valida por sí sola todos los certificados del mundo",
        "correct": "A",
        "explanation": "La aplicación cliente puede realizar la operación local; eIDAS distingue la aplicación del prestador y del servicio de confianza."
    },
    {
        "topic_num": 9,
        "question": "¿Qué diferencia hay entre un prestador de servicios de confianza y una aplicación de firma?",
        "option_a": "El prestador ofrece servicios regulados y sujeto a requisitos eIDAS; la aplicación es una herramienta cliente que puede utilizarse para ejecutar una firma",
        "option_b": "Son necesariamente la misma entidad",
        "option_c": "La aplicación es siempre una autoridad de certificación",
        "option_d": "El prestador solo proporciona hardware",
        "correct": "A",
        "explanation": "eIDAS define al prestador y sus obligaciones, mientras que una aplicación cliente no adquiere por ello esa condición jurídica."
    },
    {
        "topic_num": 9,
        "question": "¿Qué debe poder hacer un prestador cualificado al verificar la identidad?",
        "option_a": "Verificar la identidad de la persona física o jurídica a la que expide un certificado o presta el servicio conforme a los métodos admitidos",
        "option_b": "Emitir certificados sin identificar al titular",
        "option_c": "Aceptar cualquier alias sin control",
        "option_d": "Delegar toda identificación en el firmante",
        "correct": "A",
        "explanation": "El artículo 24 exige requisitos de identificación y comprobación para prestadores de servicios de confianza."
    },
    {
        "topic_num": 9,
        "question": "¿Qué efecto tiene un sello electrónico cualificado?",
        "option_a": "Disfruta de la presunción de integridad de los datos y de la corrección del origen de los datos a los que está vinculado",
        "option_b": "Solo identifica a una persona física",
        "option_c": "No tiene ningún efecto probatorio",
        "option_d": "Es una contraseña de acceso",
        "correct": "A",
        "explanation": "El artículo 35 regula los efectos del sello electrónico cualificado y su presunción de integridad y origen."
    },
    {
        "topic_num": 9,
        "question": "¿Qué es una lista de confianza?",
        "option_a": "Una lista publicada por un Estado miembro con información sobre los prestadores cualificados y los servicios cualificados supervisados",
        "option_b": "Una lista privada de contraseñas",
        "option_c": "Un registro de todos los ciudadanos",
        "option_d": "Una lista de certificados caducados únicamente",
        "correct": "A",
        "explanation": "El artículo 22 regula las listas de confianza con información sobre prestadores cualificados y servicios cualificados."
    },
    {
        "topic_num": 9,
        "question": "¿Qué finalidad tiene un sello de tiempo electrónico?",
        "option_a": "Vincular otros datos a una fecha y hora de forma que se pueda demostrar razonablemente que existían en ese momento",
        "option_b": "Cifrar una base de datos sin fecha",
        "option_c": "Sustituir siempre una firma personal",
        "option_d": "Identificar el domicilio del firmante",
        "correct": "A",
        "explanation": "El artículo 3 define el sello de tiempo electrónico como una vinculación de datos con fecha y hora para demostrar su existencia temporal."
    },
    {
        "topic_num": 9,
        "question": "¿Qué afirmación es correcta sobre una firma electrónica no cualificada?",
        "option_a": "No puede rechazarse como prueba por el mero hecho de ser electrónica o no cualificada, aunque no tenga automáticamente la equivalencia del artículo 25.2",
        "option_b": "Es siempre nula",
        "option_c": "Tiene automáticamente equivalencia manuscrita",
        "option_d": "Solo vale si se imprime",
        "correct": "A",
        "explanation": "El artículo 25.1 contiene la regla de admisibilidad; la equivalencia específica del apartado 2 corresponde a firmas cualificadas."
    },
    {
        "topic_num": 9,
        "question": "¿Qué debe conservar un servicio cualificado de conservación de firmas?",
        "option_a": "Información suficiente para prolongar la fiabilidad de la firma más allá del periodo de validez tecnológica, conforme al artículo 34",
        "option_b": "Solo la imagen de la firma",
        "option_c": "La contraseña del firmante",
        "option_d": "Ningún dato de validación",
        "correct": "A",
        "explanation": "El artículo 34 regula los servicios cualificados de conservación de firmas electrónicas cualificadas."
    },
    {
        "topic_num": 9,
        "question": "¿Qué es un certificado de sello electrónico frente a uno de firma?",
        "option_a": "El primero se expide a una persona jurídica para crear sellos; el segundo se vincula a una persona física para crear firmas",
        "option_b": "Ambos se expiden siempre al mismo sujeto",
        "option_c": "El certificado de sello solo sirve para cifrar",
        "option_d": "El de firma solo puede pertenecer a una empresa",
        "correct": "A",
        "explanation": "eIDAS distingue certificados cualificados de firma y de sello según el titular y los datos de creación asociados."
    },
    {
        "topic_num": 9,
        "question": "¿Qué dato debe acompañar a una pregunta version-sensitive sobre AutoFirma para ser publicable?",
        "option_a": "La versión exacta, URL oficial, fecha de consulta y la función verificada",
        "option_b": "Solo el nombre AutoFirma",
        "option_c": "Una URL secundaria sin fecha",
        "option_d": "La versión supuesta por el generador",
        "correct": "A",
        "explanation": "La política de fuente exige fijar versión, URL, fecha y proveniencia para evitar atribuir a AutoFirma hechos no verificables."
    }
])
# QUESTION_BANK_ACCEPTED_TOPIC_09_LOT_01_END

# QUESTION_BANK_ACCEPTED_TOPIC_10_LOT_01_START
SEED_QUESTIONS.extend([
    {
        "topic_num": 10,
        "question": "¿Qué vincula un certificado X.509?",
        "option_a": "La identidad de un sujeto con una clave pública mediante una autoridad certificadora",
        "option_b": "Una contraseña con un archivo local",
        "option_c": "Un usuario con una dirección IP sin clave",
        "option_d": "Un certificado con una base de datos sin firma",
        "correct": "A",
        "explanation": "RFC 5280 describe el certificado como una vinculación firmada entre la identidad del sujeto y su clave pública."
    },
    {
        "topic_num": 10,
        "question": "¿Qué diferencia hay entre una autoridad certificadora y el sujeto de un certificado?",
        "option_a": "La autoridad emite y firma certificados; el sujeto es la entidad identificada por el certificado",
        "option_b": "Ambos son siempre la misma entidad",
        "option_c": "El sujeto firma a la autoridad",
        "option_d": "La autoridad solo cifra mensajes",
        "correct": "A",
        "explanation": "RFC 5280 distingue al emisor o autoridad certificadora del sujeto cuya clave pública se certifica."
    },
    {
        "topic_num": 10,
        "question": "¿Para qué sirve una lista de revocación de certificados?",
        "option_a": "Para identificar certificados revocados antes de su fecha de expiración",
        "option_b": "Para emitir claves privadas nuevas automáticamente",
        "option_c": "Para comprimir certificados",
        "option_d": "Para sustituir toda validación de cadena",
        "correct": "A",
        "explanation": "Una CRL publicada por una autoridad informa de certificados revocados y sus números de serie, conforme al modelo de RFC 5280."
    },
    {
        "topic_num": 10,
        "question": "¿Cuál es un campo básico de un certificado X.509?",
        "option_a": "El nombre del sujeto, el emisor, el periodo de validez y la clave pública del sujeto",
        "option_b": "La contraseña del usuario",
        "option_c": "El contenido completo del disco",
        "option_d": "La clave privada de la autoridad",
        "correct": "A",
        "explanation": "RFC 5280 estructura el certificado con versión, número de serie, emisor, validez, sujeto, información de clave pública y firma."
    },
    {
        "topic_num": 10,
        "question": "¿Qué función cumple la extensión Key Usage?",
        "option_a": "Restringir los usos criptográficos permitidos para la clave certificada, como firma digital o cifrado de claves",
        "option_b": "Indicar el domicilio postal del titular",
        "option_c": "Revocar el certificado sin CRL",
        "option_d": "Almacenar la clave privada",
        "correct": "A",
        "explanation": "RFC 5280 define Key Usage como extensión que indica los usos permitidos de la clave pública."
    },
    {
        "topic_num": 10,
        "question": "¿Qué caracteriza a un certificado autofirmado?",
        "option_a": "La firma del certificado se verifica con la propia clave pública incluida o asociada al sujeto",
        "option_b": "Siempre lo firma una CA externa",
        "option_c": "No contiene firma",
        "option_d": "Solo puede utilizarse para correo",
        "correct": "A",
        "explanation": "En un certificado autofirmado, el emisor y el sujeto coinciden normalmente y la firma se valida con la propia clave pública."
    },
    {
        "topic_num": 10,
        "question": "¿Qué versión de TLS especifica RFC 8446?",
        "option_a": "TLS 1.3",
        "option_b": "TLS 1.0",
        "option_c": "SSL 3.0",
        "option_d": "TLS 2.0",
        "correct": "A",
        "explanation": "RFC 8446 es la especificación del protocolo Transport Layer Security versión 1.3."
    },
    {
        "topic_num": 10,
        "question": "¿Qué negocia el handshake de TLS 1.3?",
        "option_a": "Las versiones y parámetros criptográficos, autenticación y claves necesarias para proteger la conexión",
        "option_b": "La estructura de tablas SQL",
        "option_c": "Solo la dirección IP",
        "option_d": "Únicamente el idioma de la aplicación",
        "correct": "A",
        "explanation": "El handshake de TLS 1.3 establece parámetros, autentica el servidor cuando procede y deriva secretos para la protección de registros."
    },
    {
        "topic_num": 10,
        "question": "¿Qué propiedad proporciona el cifrado autenticado usado en los registros TLS 1.3?",
        "option_a": "Confidencialidad e integridad autenticada de los datos del registro",
        "option_b": "Solo compresión",
        "option_c": "Solo ocultación del nombre del servidor",
        "option_d": "Únicamente autenticación del usuario final",
        "correct": "A",
        "explanation": "RFC 8446 usa algoritmos AEAD para proteger los registros con confidencialidad e integridad autenticada."
    },
    {
        "topic_num": 10,
        "question": "¿Qué riesgo debe considerarse al usar 0-RTT en TLS 1.3?",
        "option_a": "Los datos tempranos pueden ser susceptibles de reproducción, por lo que la aplicación debe limitar sus usos",
        "option_b": "Que el certificado se convierta en una clave privada",
        "option_c": "Que TLS deje de cifrar todos los registros",
        "option_d": "Que solo funcione con HTTP/1.0",
        "correct": "A",
        "explanation": "RFC 8446 advierte de las propiedades de replay del early data y exige que los protocolos superiores lo tengan en cuenta."
    },
    {
        "topic_num": 10,
        "question": "¿Qué es una clave pública transferible en OpenPGP?",
        "option_a": "Una estructura que contiene una clave pública y los datos asociados, incluidas identidades y firmas según corresponda",
        "option_b": "Una clave privada enviada sin cifrar",
        "option_c": "Una CRL X.509",
        "option_d": "Un paquete TLS",
        "correct": "A",
        "explanation": "RFC 9580 define estructuras de claves públicas transferibles que pueden incluir claves, identidades y firmas de enlace."
    },
    {
        "topic_num": 10,
        "question": "¿Qué diferencia básica hay entre una firma OpenPGP y el cifrado OpenPGP?",
        "option_a": "La firma permite verificar origen e integridad; el cifrado busca confidencialidad para destinatarios autorizados",
        "option_b": "Ambos solo comprimen datos",
        "option_c": "El cifrado prueba siempre la identidad del emisor",
        "option_d": "La firma oculta necesariamente el contenido",
        "correct": "A",
        "explanation": "RFC 9580 trata firmas como mecanismos de autenticidad/integridad y cifrado como protección de confidencialidad."
    },
    {
        "topic_num": 10,
        "question": "¿Qué finalidad tiene una clave de revocación OpenPGP?",
        "option_a": "Permitir revocar una clave o identidad cuando la autoridad de revocación correspondiente se utiliza",
        "option_b": "Renovar automáticamente cualquier certificado TLS",
        "option_c": "Cifrar la clave pública",
        "option_d": "Sustituir las firmas de identidad",
        "correct": "A",
        "explanation": "RFC 9580 define la información de clave de revocación para permitir una revocación autorizada."
    },
    {
        "topic_num": 10,
        "question": "¿Qué permite comprobar una firma digital OpenPGP?",
        "option_a": "Que los datos fueron firmados por quien controla la clave correspondiente y no han cambiado, si la clave es confiable",
        "option_b": "Que el canal de red es siempre TLS",
        "option_c": "Que el documento está libre de malware",
        "option_d": "Que el destinatario leyó el mensaje",
        "correct": "A",
        "explanation": "La firma digital permite comprobar integridad y asociación con la clave firmante; la confianza en la identidad requiere el modelo de OpenPGP."
    },
    {
        "topic_num": 10,
        "question": "¿Qué relación hay entre clave pública y clave secreta en OpenPGP?",
        "option_a": "Forman un par criptográfico para operaciones complementarias como verificación/firma o cifrado/descifrado",
        "option_b": "Son dos copias públicas de la misma contraseña",
        "option_c": "La clave secreta se publica siempre",
        "option_d": "No tienen relación matemática",
        "correct": "A",
        "explanation": "RFC 9580 distingue material público y secreto de los pares de claves OpenPGP y sus usos complementarios."
    },
    {
        "topic_num": 10,
        "question": "¿Qué diferencia hay entre validación de certificado y cifrado?",
        "option_a": "La validación comprueba la cadena, firmas, nombres, fechas y restricciones; el cifrado protege la confidencialidad de datos",
        "option_b": "La validación siempre cifra el certificado",
        "option_c": "El cifrado confirma por sí solo la identidad",
        "option_d": "Son sinónimos",
        "correct": "A",
        "explanation": "RFC 5280 describe la validación de rutas; cifrar es una operación distinta que no sustituye la comprobación de confianza."
    },
    {
        "topic_num": 10,
        "question": "¿Por qué una validación de ruta de certificados necesita un ancla de confianza?",
        "option_a": "Porque la ruta debe terminar en una autoridad cuya clave y confianza se configuran fuera de la ruta que se está validando",
        "option_b": "Porque todas las claves se confían automáticamente",
        "option_c": "Porque el ancla contiene la contraseña del usuario",
        "option_d": "Porque evita comprobar expiración",
        "correct": "A",
        "explanation": "RFC 5280 define la validación respecto de trust anchors preconfigurados, no obtenidos como una certificación más de la misma ruta."
    },
    {
        "topic_num": 10,
        "question": "¿Qué versión negocia TLS 1.3 cuando se completa un handshake conforme a RFC 8446?",
        "option_a": "TLS 1.3, sin negociar las versiones obsoletas como si fueran la versión de la conexión",
        "option_b": "SSL 3.0",
        "option_c": "TLS 1.0 exclusivamente",
        "option_d": "Una versión elegida por el certificado",
        "correct": "A",
        "explanation": "RFC 8446 define TLS 1.3 y su negociación mediante supported_versions, separando la versión real de compatibilidades heredadas."
    },
    {
        "topic_num": 10,
        "question": "Si un certificado solo autoriza digitalSignature mediante Key Usage, ¿qué debe hacer un verificador?",
        "option_a": "No usarlo para una finalidad incompatible con las restricciones de Key Usage",
        "option_b": "Ignorar siempre la extensión",
        "option_c": "Usarlo para cualquier cifrado de clave",
        "option_d": "Considerarlo automáticamente revocado",
        "correct": "A",
        "explanation": "Las restricciones de Key Usage son parte de la validación y deben respetarse para el uso propuesto."
    },
    {
        "topic_num": 10,
        "question": "¿Qué afirmación evita confluir los modelos de confianza de PKI, TLS y OpenPGP?",
        "option_a": "X.509/PKI valida rutas de certificados, TLS protege una conexión negociada y OpenPGP usa asociaciones de claves y firmas propias",
        "option_b": "Los tres siempre usan la misma autoridad certificadora",
        "option_c": "TLS sustituye las firmas OpenPGP",
        "option_d": "OpenPGP es solo una versión de TLS",
        "correct": "A",
        "explanation": "RFC 5280, RFC 8446 y RFC 9580 describen mecanismos relacionados con criptografía, pero con objetivos y modelos de confianza distintos."
    }
])
# QUESTION_BANK_ACCEPTED_TOPIC_10_LOT_01_END

# QUESTION_BANK_ACCEPTED_TOPIC_11_LOT_01_START
SEED_QUESTIONS.extend([
    {
        "topic_num": 11,
        "question": "¿Cuál es el objeto del Esquema Nacional de Seguridad?",
        "option_a": "Establecer los principios y requisitos necesarios para una protección adecuada de la información y los servicios utilizados por las entidades de su ámbito",
        "option_b": "Regular solo la contratación privada",
        "option_c": "Sustituir la protección de datos",
        "option_d": "Regular únicamente la firma electrónica",
        "correct": "A",
        "explanation": "El Real Decreto 311/2022 establece el ENS para fundamentar la confianza en el uso de medios electrónicos mediante protección adecuada de información y servicios."
    },
    {
        "topic_num": 11,
        "question": "¿Qué exige el principio de seguridad como función diferenciada en el ENS?",
        "option_a": "Una protección basada en medidas adecuadas al riesgo y en la prevención, detección, respuesta y conservación",
        "option_b": "Solo instalar antivirus",
        "option_c": "No documentar incidentes",
        "option_d": "Proteger únicamente la confidencialidad",
        "correct": "A",
        "explanation": "El ENS exige una protección integral y proporcional, con prevención, detección, respuesta y conservación frente a riesgos."
    },
    {
        "topic_num": 11,
        "question": "¿Cómo deben ser las medidas de seguridad del ENS?",
        "option_a": "Proporcionadas a los riesgos y a la categoría del sistema, considerando la naturaleza de la información y los servicios",
        "option_b": "Idénticas para todos los sistemas sin análisis",
        "option_c": "Solo voluntarias para el sector público",
        "option_d": "Aplicables únicamente después de un incidente",
        "correct": "A",
        "explanation": "El ENS vincula las medidas al análisis de riesgos y a la categoría del sistema, sin reducir la protección a una configuración idéntica."
    },
    {
        "topic_num": 11,
        "question": "¿Qué instrumento recoge las directrices de seguridad de una organización?",
        "option_a": "La política de seguridad, aprobada por el órgano competente y aplicable al ámbito de la organización",
        "option_b": "Una contraseña individual",
        "option_c": "Un informe de auditoría externo solamente",
        "option_d": "El inventario de hardware",
        "correct": "A",
        "explanation": "La política de seguridad establece las directrices de seguridad de la organización y debe aprobarse por el órgano competente."
    },
    {
        "topic_num": 11,
        "question": "¿Qué responsabilidades deben diferenciarse en la gobernanza de la seguridad?",
        "option_a": "Las responsabilidades sobre la información, los servicios, la seguridad y los sistemas, sin perjuicio de las estructuras organizativas",
        "option_b": "Una única responsabilidad siempre atribuida al usuario",
        "option_c": "Solo la responsabilidad del proveedor externo",
        "option_d": "Ninguna responsabilidad documentada",
        "correct": "A",
        "explanation": "El ENS exige una organización de la seguridad y la diferenciación de responsabilidades para información, servicios, seguridad y sistemas."
    },
    {
        "topic_num": 11,
        "question": "¿Qué categorías de seguridad contempla el ENS?",
        "option_a": "Básica, media y alta",
        "option_b": "Local, nacional y europea",
        "option_c": "Preventiva, reactiva y penal",
        "option_d": "A, B y C sin significado de riesgo",
        "correct": "A",
        "explanation": "El ENS clasifica los sistemas en categorías básica, media y alta según el impacto de un incidente sobre las dimensiones de seguridad."
    },
    {
        "topic_num": 11,
        "question": "¿Qué se tiene en cuenta para determinar la categoría de seguridad de un sistema?",
        "option_a": "El impacto que tendría un incidente sobre las dimensiones de seguridad de la información y los servicios",
        "option_b": "Solo el número de usuarios",
        "option_c": "El fabricante del servidor",
        "option_d": "El presupuesto anual",
        "correct": "A",
        "explanation": "La categoría se determina a partir de la valoración del impacto de los incidentes sobre las dimensiones de seguridad."
    },
    {
        "topic_num": 11,
        "question": "¿Qué relación hay entre el análisis de riesgos y las medidas ENS?",
        "option_a": "El análisis de riesgos informa la selección de medidas, que deben ser adecuadas y proporcionales",
        "option_b": "Las medidas se eligen sin relación con el riesgo",
        "option_c": "El análisis solo se realiza después de un ataque",
        "option_d": "El riesgo se elimina por decreto",
        "correct": "A",
        "explanation": "El principio de gestión de riesgos exige valorar amenazas y elegir medidas proporcionadas para reducirlas."
    },
    {
        "topic_num": 11,
        "question": "¿Para qué sirve la estructura de gobernanza de la seguridad?",
        "option_a": "Para coordinar, supervisar y asignar responsabilidades de seguridad dentro de la organización",
        "option_b": "Para sustituir todos los controles técnicos",
        "option_c": "Solo para publicar contratos",
        "option_d": "Para eliminar la función del responsable de seguridad",
        "correct": "A",
        "explanation": "La organización de la seguridad permite coordinar y asignar funciones, responsabilidades y decisiones de protección."
    },
    {
        "topic_num": 11,
        "question": "¿Qué documento debe describir la protección de un sistema?",
        "option_a": "El plan de adecuación o de seguridad del sistema, con las medidas y decisiones aplicables al sistema",
        "option_b": "Solo el registro de usuarios",
        "option_c": "Únicamente el contrato de mantenimiento",
        "option_d": "Una nota verbal no documentada",
        "correct": "A",
        "explanation": "El ENS exige planificar y documentar la seguridad del sistema, incluyendo medidas, responsables y decisiones de adecuación."
    },
    {
        "topic_num": 11,
        "question": "¿Qué grupos de medidas recoge el ENS?",
        "option_a": "Medidas relativas al marco organizativo, al marco operacional y a las medidas de protección",
        "option_b": "Solo medidas de hardware",
        "option_c": "Solo medidas de cifrado",
        "option_d": "Medidas exclusivamente presupuestarias",
        "correct": "A",
        "explanation": "El anexo II estructura el marco de medidas en organizativas, operacionales y de protección."
    },
    {
        "topic_num": 11,
        "question": "¿Qué control se asocia especialmente a sistemas de categoría alta?",
        "option_a": "La auditoría de seguridad y, cuando proceda, la certificación o evaluación de conformidad conforme al ENS",
        "option_b": "Solo una autoevaluación informal",
        "option_c": "Ningún control adicional",
        "option_d": "Una encuesta a usuarios",
        "correct": "A",
        "explanation": "El ENS prevé auditorías y evaluaciones de conformidad con exigencias reforzadas según la categoría del sistema."
    },
    {
        "topic_num": 11,
        "question": "¿Qué exige el ENS respecto de la seguridad a lo largo del tiempo?",
        "option_a": "Revisión, actualización y mejora continua mediante monitorización y reevaluación periódica",
        "option_b": "Configurar una vez y no volver a revisar",
        "option_c": "Revisar solo cuando cambie el nombre del sistema",
        "option_d": "No conservar registros",
        "correct": "A",
        "explanation": "El ENS aplica un ciclo de mejora continua y exige revisar la seguridad ante cambios, incidentes y evolución del riesgo."
    },
    {
        "topic_num": 11,
        "question": "¿Qué función cumple la gestión de incidentes de seguridad?",
        "option_a": "Detectar, analizar, responder y aprender de incidentes, comunicándolos por los canales establecidos",
        "option_b": "Ocultar cualquier incidente",
        "option_c": "Sustituir las medidas preventivas",
        "option_d": "Registrar solo incidentes de usuarios externos",
        "correct": "A",
        "explanation": "La gestión de incidentes es una capacidad de respuesta y mejora, con comunicaciones según los procedimientos y autoridades aplicables."
    },
    {
        "topic_num": 11,
        "question": "¿Qué implica aplicar el principio de mínimo privilegio?",
        "option_a": "Conceder a cada usuario o proceso solo los permisos necesarios para sus funciones",
        "option_b": "Conceder permisos de administrador a todos",
        "option_c": "No revisar permisos nunca",
        "option_d": "Permitir acceso anónimo a datos sensibles",
        "correct": "A",
        "explanation": "El control de acceso debe limitar los privilegios a los necesarios, reduciendo la superficie de ataque y el impacto de errores."
    },
    {
        "topic_num": 11,
        "question": "¿Qué dimensión puede verse afectada por un incidente de seguridad?",
        "option_a": "Confidencialidad, integridad, autenticidad, trazabilidad o disponibilidad, según el marco aplicable",
        "option_b": "Solo la disponibilidad",
        "option_c": "Solo el coste económico",
        "option_d": "Ninguna si existe copia de seguridad",
        "correct": "A",
        "explanation": "El ENS trabaja con dimensiones de seguridad que permiten valorar impactos más allá de la mera disponibilidad."
    },
    {
        "topic_num": 11,
        "question": "¿Qué debe proteger el ENS?",
        "option_a": "La información tratada y los servicios prestados mediante sistemas, junto con los elementos que los soportan",
        "option_b": "Solo los ordenadores personales",
        "option_c": "Exclusivamente los datos publicados",
        "option_d": "Solo el perímetro físico",
        "correct": "A",
        "explanation": "El ámbito material del ENS comprende la información y los servicios y los sistemas que los soportan."
    },
    {
        "topic_num": 11,
        "question": "¿Por qué el cumplimiento del ENS no es una configuración única?",
        "option_a": "Porque exige gestión continua, análisis de cambios, incidentes, auditorías y mejora de medidas",
        "option_b": "Porque solo se revisa cada veinte años",
        "option_c": "Porque no requiere documentación",
        "option_d": "Porque las categorías no cambian nunca",
        "correct": "A",
        "explanation": "La adecuación al ENS requiere un proceso permanente de gestión y revisión, no una instalación aislada."
    },
    {
        "topic_num": 11,
        "question": "¿Qué función tiene una entidad de evaluación de la conformidad?",
        "option_a": "Evaluar o auditar la conformidad con los requisitos aplicables conforme al esquema de certificación",
        "option_b": "Asignar por sí sola la categoría a todos los sistemas",
        "option_c": "Sustituir al responsable del sistema",
        "option_d": "Crear leyes",
        "correct": "A",
        "explanation": "El ENS contempla la evaluación y certificación de conformidad por entidades y procedimientos reconocidos."
    },
    {
        "topic_num": 11,
        "question": "¿Qué debe hacer una organización ante un incidente ENS relevante?",
        "option_a": "Gestionarlo y comunicarlo por los canales y procedimientos establecidos, conservando la información necesaria",
        "option_b": "Borrarlo para evitar auditorías",
        "option_c": "Esperar siempre al cierre del ejercicio",
        "option_d": "Informar solo a los usuarios afectados sin análisis",
        "correct": "A",
        "explanation": "El artículo 26 exige procedimientos de gestión y comunicación de incidentes de seguridad."
    }
])
# QUESTION_BANK_ACCEPTED_TOPIC_11_LOT_01_END
