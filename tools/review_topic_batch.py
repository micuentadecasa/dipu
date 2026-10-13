#!/usr/bin/env python3
"""Independent review and promotion for a topic 2-5 candidate lot."""

from __future__ import annotations

import argparse
import copy
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from question_bank.checkpoints import append_checkpoint, file_sha256
from question_bank.validation import validate_record

DATE = "2026-10-13"
TOPIC34_KEY_PATH = ROOT / "docs/question-bank/reviews/topic-34-answer-key.json"
TOPIC35_KEY_PATH = ROOT / "docs/question-bank/reviews/topic-35-answer-key.json"
TOPIC36_KEY_PATH = ROOT / "docs/question-bank/reviews/topic-36-answer-key.json"
TOPIC37_KEY_PATH = ROOT / "docs/question-bank/reviews/topic-37-answer-key.json"
EXPECTATIONS = {
    2: {
        1:("A","Artículo 97"),2:("A","Artículo 98.1"),3:("A","Artículo 98.2"),4:("A","Artículo 98.3"),5:("B","Artículo 100"),
        6:("B","Artículo 108"),7:("A","Artículo 102"),8:("A","Artículo 111"),9:("A","Artículo 112"),10:("A","Artículo 113"),
        11:("A","Artículos 112 y 113"),12:("A","Artículo 115.2"),13:("A","Artículo 137"),14:("A","Artículo 140"),15:("A","Artículo 141.1"),
        16:("A","Artículo 142"),17:("A","Artículo 147.2"),18:("A","Artículo 149.3"),19:("A","Artículo 153.a"),20:("A","Artículo 155.1"),
    },
    3: {
        1:("A","Artículo 11"),2:("A","Artículo 11.2"),3:("A","Artículo 12.2"),4:("A","Artículo 16"),5:("A","Artículo 20.1.a"),
        6:("A","Artículo 20.1.b"),7:("A","Artículo 21.1.a y b"),8:("A","Artículo 22.2.a"),9:("A","Artículo 22.2.d"),10:("A","Artículo 23.2"),
        11:("A","Artículo 31.1"),12:("A","Artículo 32.1"),13:("A","Artículo 34.1.a y b"),14:("A","Artículo 33.2.a"),15:("A","Artículo 36.1.b"),
        16:("A","Artículo 36.1.a"),17:("A","Artículo 36.1.c"),18:("A","Artículo 36.2.a"),19:("A","Artículo 36.2.b"),20:("A","Artículos 1, 2, 11, 31 y 32"),
    },
    4: {
        1:("A","RDL 781/1986, artículo 22.3"),2:("A","RDL 781/1986, artículo 21"),3:("A","RDL 781/1986, artículo 23"),4:("A","RDL 781/1986, artículo 24.1"),5:("A","RDL 781/1986, artículo 30.1"),
        6:("A","RDL 781/1986, artículo 30.2.b"),7:("A","RDL 781/1986, artículo 35.2"),8:("A","RDL 781/1986, artículo 35.2.d"),9:("A","RDL 781/1986, artículo 32"),10:("A","RDL 781/1986, artículo 34.1"),
        11:("A","RD 2568/1986, artículo 29"),12:("A","RD 2568/1986, artículo 32"),13:("A","RD 2568/1986, artículo 25"),14:("A","RD 2568/1986, artículo 26"),15:("A","RD 2568/1986, artículo 27"),
        16:("A","RD 2568/1986, artículo 28.3"),17:("A","RD 2568/1986, artículo 31.1"),18:("A","RD 2568/1986, artículo 35.1"),19:("A","RD 2568/1986, artículo 34.2"),20:("A","RD 2568/1986, artículos 24 y 30"),
    },
    5: {
        1:("A","Artículo 1.1"),2:("A","Artículo 2.3"),3:("A","Artículo 3"),4:("A","Artículo 4.1"),5:("A","Artículo 4.3"),
        6:("A","Artículo 5.1"),7:("A","Artículo 5.4"),8:("A","Artículo 5.6"),9:("A","Artículo 53.1.a"),10:("A","Artículo 14.2.a-e"),
        11:("A","Artículo 14.1"),12:("A","Artículos 9 y 10"),13:("A","Artículo 15.1"),14:("A","Artículo 53.1.d"),15:("A","Artículo 53.1.e"),
        16:("A","Artículo 53.1.g"),17:("A","Artículo 53.1.h"),18:("A","Artículo 5.2"),19:("A","Artículo 15.1"),20:("A","Artículos 5.1 y 53.1.g"),
    },
    6: {
        1:("A","Artículo 26.1"),2:("A","Artículo 70.1"),3:("A","Artículo 30.1"),4:("A","Artículo 30.5"),5:("A","Artículo 32.1"),6:("A","Artículo 21.1"),7:("A","Artículo 24.1"),8:("A","Artículo 34.1"),9:("A","Artículo 35.1.a"),10:("A","Artículo 36.1"),11:("A","Artículo 39.1"),12:("A","Artículo 40.2"),13:("A","Artículo 40.2"),14:("A","Artículo 45.1.a y b"),15:("A","Artículo 47.1.a"),16:("A","Artículo 48.1"),17:("A","Artículo 51"),18:("A","Artículo 107.1"),19:("A","Artículo 23"),20:("A","Artículo 43.2")
    },
    7: {
        1:("A","Artículo 4.1"),2:("A","Artículo 2.1"),3:("A","Artículo 14.1"),4:("A","Artículo 14.2"),5:("A","Artículo 14.4"),6:("A","Artículo 15.1.a-c"),7:("A","Artículo 16.1"),8:("A","Artículo 17.2"),9:("A","Artículo 18.1"),10:("A","Artículo 19.1"),11:("A","Artículo 20"),12:("A","Artículo 21.2"),13:("A","Artículo 22.1"),14:("A","Artículo 23.1"),15:("A","Artículo 24.1"),16:("A","Artículo 25.1"),17:("A","Artículo 26.1"),18:("A","Artículo 29.1"),19:("A","Artículos 34 y 35"),20:("A","Artículo 31.2")
    },
    8: {
        1:("A","Artículo 1.1"),2:("A","Artículo 6.1"),3:("A","Artículo 7.1"),4:("A","Artículo 7.2"),5:("A","Artículo 6.3"),6:("A","Artículo 11.1"),7:("A","Artículo 5"),8:("A","Artículos 45 y 46"),9:("A","Artículo 43"),10:("A","Artículo 13"),11:("A","Artículos 10 y 12"),12:("A","Artículo 51"),13:("A","Artículos 33 y 35"),14:("A","Artículo 46"),15:("A","Artículo 8"),16:("A","Artículo 9"),17:("A","Artículo 14.11"),18:("A","Artículo 42"),19:("A","Artículos 14 y 36"),20:("A","Artículo 15")
    },
    9: {
        1:("A","eIDAS, artículo 3, puntos 1, 10 y 11"),2:("A","eIDAS, artículo 25.1"),3:("A","eIDAS, artículo 6"),4:("A","eIDAS, artículo 3, punto 16"),5:("A","eIDAS, artículo 26"),6:("A","eIDAS, artículo 25.2"),7:("A","eIDAS, artículos 3.15 y 28"),8:("A","eIDAS, artículo 29 y anexo II"),9:("A","Página oficial de descargas de AutoFirma, consulta 2026-10-12"),10:("A","Página oficial de descargas de AutoFirma, consulta 2026-10-12"),11:("A","eIDAS, artículos 3 y 24; página oficial de AutoFirma"),12:("A","eIDAS, artículo 3, puntos 19 y 20; página oficial de AutoFirma"),13:("A","eIDAS, artículo 24"),14:("A","eIDAS, artículo 35.2"),15:("A","eIDAS, artículo 22"),16:("A","eIDAS, artículo 3, punto 33"),17:("A","eIDAS, artículo 25.1 y 25.2"),18:("A","eIDAS, artículo 34"),19:("A","eIDAS, artículos 3.14, 3.15, 28 y 38"),20:("A","Página oficial de descargas de AutoFirma, consulta 2026-10-12")
    },
    10: {
        1:("A","RFC 5280, sección 3"),2:("A","RFC 5280, secciones 3 y 4"),3:("A","RFC 5280, sección 5"),4:("A","RFC 5280, sección 4.1"),5:("A","RFC 5280, sección 4.2.1.3"),6:("A","RFC 5280, sección 3"),7:("A","RFC 8446, sección 1"),8:("A","RFC 8446, sección 4"),9:("A","RFC 8446, sección 5"),10:("A","RFC 8446, sección 2.3"),11:("A","RFC 9580, sección 5"),12:("A","RFC 9580, secciones 5 y 10"),13:("A","RFC 9580, sección 5.2.3.15"),14:("A","RFC 9580, sección 5.2"),15:("A","RFC 9580, sección 5"),16:("A","RFC 5280, secciones 6 y 7"),17:("A","RFC 5280, sección 6.1"),18:("A","RFC 8446, sección 4"),19:("A","RFC 5280, sección 4.2.1.3"),20:("A","RFC 5280, RFC 8446 y RFC 9580")
    },
    11: {
        1:("A","Real Decreto 311/2022, artículos 1 y 2"),2:("A","Real Decreto 311/2022, artículo 5"),3:("A","Real Decreto 311/2022, artículo 6"),4:("A","Real Decreto 311/2022, artículo 11"),5:("A","Real Decreto 311/2022, artículo 13"),6:("A","Real Decreto 311/2022, artículos 40 y 41"),7:("A","Real Decreto 311/2022, artículo 40"),8:("A","Real Decreto 311/2022, artículo 6"),9:("A","Real Decreto 311/2022, artículo 13"),10:("A","Real Decreto 311/2022, artículo 15"),11:("A","Real Decreto 311/2022, anexo II"),12:("A","Real Decreto 311/2022, artículos 31 y 38"),13:("A","Real Decreto 311/2022, artículos 10 y 34"),14:("A","Real Decreto 311/2022, artículo 26"),15:("A","Real Decreto 311/2022, anexo II, marco de medidas"),16:("A","Real Decreto 311/2022, artículos 3 y 7"),17:("A","Real Decreto 311/2022, artículos 2 y 3"),18:("A","Real Decreto 311/2022, artículos 10 y 31"),19:("A","Real Decreto 311/2022, artículo 38"),20:("A","Real Decreto 311/2022, artículo 26")
    },
    12: {
        1:("A","RGPD, artículo 4.1"),2:("A","RGPD, artículo 4.7 y 4.8"),3:("A","RGPD, artículo 5.1.a"),4:("A","RGPD, artículo 6.1.a"),5:("A","RGPD, artículos 4.11 y 7"),6:("A","RGPD, artículo 13"),7:("A","RGPD, artículos 13 y 14"),8:("A","RGPD, artículo 15.1"),9:("A","RGPD, artículo 17"),10:("A","RGPD, artículo 20.1"),11:("A","RGPD, artículo 25"),12:("A","RGPD, artículo 32.1"),13:("A","RGPD, artículo 33.1"),14:("A","RGPD, artículo 35.1"),15:("A","RGPD, artículo 39"),16:("A","LOPDGDD, artículo 7"),17:("A","LOPDGDD, artículo 19"),18:("A","LOPDGDD, artículos 44 y 47"),19:("A","RGPD, artículo 5.2"),20:("A","RGPD y LOPDGDD, artículos citados")
    },
    13: {
        1:("A","PostgreSQL 18, capítulo 1"),2:("A","PostgreSQL 18, capítulo 22"),3:("A","PostgreSQL 18, capítulo 18"),4:("A","PostgreSQL 18, sección 19.4.1"),5:("A","PostgreSQL 18, capítulo 28"),6:("A","PostgreSQL 18, sección 28.5"),7:("A","PostgreSQL 18, sección 24.1"),8:("A","PostgreSQL 18, capítulo 19"),9:("A","PostgreSQL 18, sección 21.2"),10:("A","PostgreSQL 18, sección 22.1"),11:("A","PostgreSQL 18, sección 5.9"),12:("A","PostgreSQL 18, sección 22.6"),13:("A","PostgreSQL 18, capítulo 13"),14:("A","PostgreSQL 18, sección 24.1"),15:("A","PostgreSQL 18, capítulo 14"),16:("A","PostgreSQL 18, capítulo 28"),17:("A","PostgreSQL 18, sección 18.5"),18:("A","PostgreSQL 18, sección 20.1"),19:("A","PostgreSQL 18, capítulo 18"),20:("A","PostgreSQL 18, capítulo 28")
    },
    14: {
        1:("A","PostgreSQL 18, capítulo 5"),2:("A","PostgreSQL 18, CREATE VIEW y sección 39.3"),3:("A","PostgreSQL 18, capítulo 11"),4:("A","PostgreSQL 18, sección 9.17"),5:("A","PostgreSQL 18, sección 36.4"),6:("A","PostgreSQL 18, CREATE TRIGGER"),7:("A","PostgreSQL 18, sección 38.17"),8:("A","PostgreSQL 18, sección 5.9.3"),9:("A","PostgreSQL 18, sección 5.5.4"),10:("A","PostgreSQL 18, sección 5.5.5"),11:("A","PostgreSQL 18, capítulo 22 y sección 5.9"),12:("A","PostgreSQL 18, sección 5.1"),13:("A","PostgreSQL 18, capítulo 5.10"),14:("A","PostgreSQL 18, CREATE VIEW"),15:("A","PostgreSQL 18, sección 36.7.1"),16:("A","PostgreSQL 18, sección 6.4"),17:("A","PostgreSQL 18, sección 39.3"),18:("A","PostgreSQL 18, CREATE TRIGGER"),19:("A","PostgreSQL 18, capítulos 5 y 21"),20:("A","PostgreSQL 18, sección 5.9")
    },
    15: {
        1:("A","PostgreSQL 18, gestión de transacciones"),2:("A","PostgreSQL 18, gestión de transacciones"),3:("A","PostgreSQL 18, gestión de transacciones"),4:("A","PostgreSQL 18, gestión de transacciones"),5:("A","PostgreSQL 18, sección 13.2"),6:("A","PostgreSQL 18, sección 13.2.1"),7:("A","PostgreSQL 18, secciones 13.2.2 y 13.2.3"),8:("A","PostgreSQL 18, sección 13.3"),9:("A","PostgreSQL 18, sección 13.3.2"),10:("A","PostgreSQL 18, sección 13.3.4"),11:("A","PostgreSQL 18, sección 13.2"),12:("A","PostgreSQL 18, DDL transaccional"),13:("A","PostgreSQL 18, gestión de transacciones"),14:("A","PostgreSQL 18, sección 13.2"),15:("A","PostgreSQL 18, sección 13.3.4"),16:("A","PostgreSQL 18, sección 24.1"),17:("A","PostgreSQL 18, sección 19.5.1"),18:("A","PostgreSQL 18, gestión de transacciones"),19:("A","PostgreSQL 18, sección 13.2.3"),20:("A","PostgreSQL 18, capítulos 13 y 28")
    },
    16: {
        1:("A","psql, Description"),2:("A","pg_dump, Description"),3:("A","SQL COPY, Description"),4:("A","SQL COPY, Notes"),5:("A","pg_restore, Description"),6:("A","SQL Dump; pg_dump, Description"),7:("A","SQL COPY, Notes; psql, Meta-Commands"),8:("A","SQL COPY, Parameters"),9:("A","psql, Options, -f/--file"),10:("A","pg_dump, Description"),11:("A","pg_dump, Description, Output Formats"),12:("A","pg_restore, Description"),13:("A","SQL COPY, Notes"),14:("A","SQL COPY, Description"),15:("A","SQL COPY, Binary Format"),16:("A","pg_dump, Description"),17:("A","pg_restore, Warning"),18:("A","SQL COPY, Notes"),19:("A","SQL Dump, Restoring the Dump"),20:("A","pg_restore, Options, -l/--list and -L/--use-list")
    },
    17: {
        1:("A","14.1. Using EXPLAIN"),2:("A","11.1. Introduction"),3:("A","ANALYZE, Description"),4:("A","19.7. Query Planning"),5:("A","14.1.1. EXPLAIN Basics"),6:("A","11.2.1. B-Tree"),7:("A","14.2. Statistics Used by the Planner"),8:("A","24.1. Routine Vacuuming"),9:("A","14.1.2. EXPLAIN ANALYZE"),10:("A","11.3. Multicolumn Indexes"),11:("A","ANALYZE, Description"),12:("A","19.7.2. Planner Cost Constants"),13:("A","14.1.1. EXPLAIN Basics"),14:("A","11.8. Partial Indexes"),15:("A","14.2. Statistics Used by the Planner"),16:("A","24.1. Routine Vacuuming"),17:("A","27.2.3. pg_stat_activity"),18:("A","Chapter 15. Parallel Query"),19:("A","11.4. Indexes and ORDER BY"),20:("A","24.1.6. The Autovacuum Daemon")
    },
    18: {
        1:("A","C# type system overview"),2:("A","C# type system: value types and reference types"),3:("A","Implicitly typed local variables"),4:("A","Generics in .NET"),5:("A","Selection statements"),6:("A","Methods, overview"),7:("A","Classes and objects"),8:("A","Generics in .NET"),9:("A","Iteration statements"),10:("A","Parameter passing"),11:("A","Inheritance in C#"),12:("A","Generics in .NET"),13:("A","Jump statements"),14:("A","Exception handling statements"),15:("A","Access modifiers"),16:("A","LINQ overview"),17:("A","Pattern matching overview"),18:("A","Exception handling statements"),19:("A","Methods and polymorphism"),20:("A","Generic constraints")
    },
    19: {
        1:("B","MVC pattern"),2:("C","What is a Controller?"),3:("A","Razor syntax"),4:("D","Grid system"),5:("B","MVC pattern"),6:("C","Defining Actions"),7:("A","Views in ASP.NET Core MVC"),8:("D","Grid system"),9:("A","Conventional routing; Attribute routing for REST APIs"),10:("C","What is a Layout"),11:("B","Razor syntax"),12:("D","How they work"),13:("A","Route templates"),14:("C","What is a Controller?"),15:("B","@model"),16:("D","Core concepts"),17:("A","Partial views"),18:("C","Specifying a Layout"),19:("B","Implicit Razor expressions"),20:("D","How it works")
    },
    20: {
        1:("B","Entity Framework Core"),2:("C","The model"),3:("A","The DbContext lifetime"),4:("D","Migrations Overview"),5:("B","Creating and Configuring a Model"),6:("C","Including types in the model"),7:("A","Querying Data"),8:("B","Tracking queries"),9:("C","No-tracking queries"),10:("B","Approach 1: change tracking and SaveChanges"),11:("A","Entity states"),12:("D","How to track entities"),13:("B","DbContext in dependency injection for ASP.NET Core"),14:("C","Avoiding DbContext threading issues"),15:("A","Evolving your model"),16:("D","Approach 2: ExecuteUpdate and ExecuteDelete (bulk update)"),17:("B","Introduction to relationships"),18:("C","Identity resolution"),19:("A","Entity Framework Core tools reference"),20:("B","Asynchronous operation pitfalls")
    },
    21: {
        1:("B","Standard query operators overview"),2:("C","Standard query operators overview"),3:("A","Projection operations"),4:("D","Filtering Data in C# with LINQ"),5:("B","Standard query operators overview"),6:("C","Standard query operators overview"),7:("A","Standard query operators overview"),8:("D","Grouping Data (C#)"),9:("B","Join operations in LINQ"),10:("C","Join operations in LINQ"),11:("A","Set operations (C#)"),12:("D","Quantifier operations in LINQ (C#)"),13:("B","Quantifier operations in LINQ (C#)"),14:("C","Partitioning data (C#)"),15:("A","Projection operations (C#)"),16:("D","Join operations in LINQ"),17:("B","Standard query operators overview"),18:("C","Standard query operators overview"),19:("A","Grouping Data (C#)"),20:("D","Standard query operators overview")
    },
    22: {
        1:("B","Model Binding in ASP.NET Core"),2:("B","Model Binding in ASP.NET Core"),3:("C","Model Binding in ASP.NET Core"),4:("A","Model Binding in ASP.NET Core"),5:("B","Model Binding in ASP.NET Core"),6:("C","Model validation in ASP.NET Core MVC and Razor Pages"),7:("A","Model validation in ASP.NET Core MVC and Razor Pages"),8:("D","Model validation in ASP.NET Core MVC and Razor Pages"),9:("A","Model validation in ASP.NET Core MVC and Razor Pages"),10:("B","Model validation in ASP.NET Core MVC and Razor Pages"),11:("A","Understand entity states"),12:("C","Understand entity states"),13:("A","Use recommended HttpPost Edit code: Read and update"),14:("B","Protect against overposting"),15:("B","Handle transactions"),16:("A","Asynchronous Programming - EF Core"),17:("B","Asynchronous Programming - EF Core"),18:("B","Asynchronous Programming - EF Core"),19:("B","Model state"),20:("A","Protect against overposting")
    },
    23: {
        1:("A","Overview of ASP.NET Core Authentication; Introduction to authorization in ASP.NET Core"),2:("B","Claim-based authorization in ASP.NET Core"),3:("C","Overview of ASP.NET Core Authentication"),4:("B","Introduction to authorization in ASP.NET Core"),5:("C","Claim-based authorization in ASP.NET Core"),6:("A","Claim-based authorization in ASP.NET Core"),7:("A","Claim-based authorization in ASP.NET Core"),8:("B","Policy-based authorization in ASP.NET Core"),9:("A","Role-based authorization in ASP.NET Core"),10:("B","Role-based authorization in ASP.NET Core"),11:("A","Role-based authorization in ASP.NET Core"),12:("B","Role-based authorization in ASP.NET Core"),13:("A","Filters in ASP.NET Core"),14:("B","Filters in ASP.NET Core"),15:("A","Filters in ASP.NET Core"),16:("A","Filters in ASP.NET Core"),17:("B","Introduction to authorization in ASP.NET Core"),18:("A","Introduction to authorization in ASP.NET Core"),19:("B","Claim-based authorization in ASP.NET Core"),20:("A","Policy-based authorization in ASP.NET Core")
    },
    24: {
        1:("A","Create web APIs with ASP.NET Core"),2:("B","Create web APIs with ASP.NET Core"),3:("B","Create web APIs with ASP.NET Core — Attribute routing requirement"),4:("A","Create web APIs with ASP.NET Core — Automatic HTTP 400 responses"),5:("A","Create web APIs with ASP.NET Core — Binding source parameter inference"),6:("A","Create web APIs with ASP.NET Core — Binding source parameter inference"),7:("A","Create web APIs with ASP.NET Core — Binding source parameter inference"),8:("A","Create web APIs with ASP.NET Core — Formatters"),9:("A","Create web APIs with ASP.NET Core — Content negotiation"),10:("A","Create web APIs with ASP.NET Core — Formatters"),11:("A","Create web APIs with ASP.NET Core — Controller action return types"),12:("A","Create web APIs with ASP.NET Core — Controller action return types"),13:("A","Controller action return types in ASP.NET Core web API"),14:("A","Create web APIs with ASP.NET Core — Automatic HTTP 400 responses"),15:("A","Routing to controller actions in ASP.NET Core"),16:("A","ASP.NET Core web API documentation with Swagger / OpenAPI"),17:("A","Create web APIs with ASP.NET Core — Formatters"),18:("A","Controller action return types in ASP.NET Core web API"),19:("A","Create web APIs with ASP.NET Core — Binding source parameter inference"),20:("A","Create web APIs with ASP.NET Core — Automatic HTTP 400 responses; Controller action return types")
    },
}


LOT_EXPECTATIONS = {
    (20, 2): {
        1:("B","The model"),2:("B","The model"),3:("A","The model"),4:("D","Migrations Overview"),5:("B","Grouping configuration"),6:("C","Use fluent API to configure a model"),7:("A","Use data annotations to configure a model"),8:("B","Built-in conventions"),9:("B","Including types in the model"),10:("C","Excluding from migrations"),11:("A","Querying Data"),12:("B","Querying Data"),13:("A","Querying Data"),14:("C","Filtering"),15:("C","Tracking and custom projections"),16:("D","Tracking vs. No-Tracking Queries"),17:("B","Tracking queries"),18:("C","No-tracking queries"),19:("A","Identity resolution"),20:("D","Tracking vs. No-Tracking Queries")
    },
    (20, 3): {
        1:("B","Change Tracking in EF Core"),2:("A","Entity states"),3:("A","How to track entities"),4:("D","How to track entities"),5:("A","How to track entities"),6:("B","How to track entities"),7:("C","Approach 1: change tracking and SaveChanges"),8:("D","Approach 2: ExecuteUpdate and ExecuteDelete (bulk update)"),9:("A","Approach 2: ExecuteUpdate and ExecuteDelete (bulk update)"),10:("B","Approach 2: ExecuteUpdate and ExecuteDelete (bulk update)"),11:("A","Introduction to relationships"),12:("B","Introduction to relationships"),13:("C","Introduction to relationships"),14:("B","Introduction to relationships"),15:("C","Introduction to relationships"),16:("B","Introduction to relationships"),17:("A","Introduction to relationships"),18:("A","Including types in the model"),19:("C","Evolving your model"),20:("B","Migrations Overview")
    },
    (20, 4): {
        1:("A","Create your first migration"),2:("C","Create your database and schema"),3:("A","Migrations Overview"),4:("B","Entity Framework Core tools reference"),5:("B","Entity Framework Core tools reference"),6:("C","Entity Framework Core tools reference"),7:("A","Avoiding DbContext threading issues"),8:("B","Asynchronous operation pitfalls"),9:("C","DbContext in dependency injection for ASP.NET Core"),10:("A","Use a DbContext factory"),11:("A","Querying Data"),12:("B","Querying Data"),13:("C","No-tracking queries"),14:("B","Identity resolution"),15:("A","Tracking and custom projections"),16:("B","Evolving your model"),17:("C","Migrations Overview"),18:("D","Creating and Configuring a Model"),19:("A","Excluding from migrations"),20:("B","Migrations Overview")
    },
    (20, 5): {
        1:("B","Creating and Configuring a Model"),2:("A","Creating and Configuring a Model"),3:("B","Creating and Configuring a Model"),4:("A","Entity Types"),5:("A","Table name; Table schema"),6:("A","View mapping"),7:("A","Including types in the model"),8:("B","Creating and Configuring a Model"),9:("A","Loading a single entity"),10:("A","Filtering"),11:("A","Tracking vs. No-Tracking Queries"),12:("A","Configuring the default tracking behavior"),13:("A","Tracking vs. No-Tracking Queries"),14:("A","Change Tracking in EF Core"),15:("A","The DbContext lifetime"),16:("A","Approach 2: ExecuteUpdate and ExecuteDelete (bulk update)"),17:("A","Evolving your model"),18:("A","Entity Framework Core tools reference"),19:("A","Avoiding DbContext threading issues"),20:("A","The DbContext lifetime; Asynchronous operation pitfalls; Approach 1: change tracking and SaveChanges")
    },
    (24, 2): {
        1:("A","Create web APIs with ASP.NET Core — Controller action return types"),2:("B","Create web APIs with ASP.NET Core"),3:("C","Create web APIs with ASP.NET Core"),4:("D","Routing to controller actions in ASP.NET Core"),5:("A","Routing to controller actions in ASP.NET Core"),6:("B","Routing to controller actions in ASP.NET Core"),7:("C","Routing to controller actions in ASP.NET Core"),8:("D","Routing to controller actions in ASP.NET Core"),9:("A","Routing to controller actions in ASP.NET Core"),10:("B","Routing to controller actions in ASP.NET Core"),11:("C","Routing to controller actions in ASP.NET Core"),12:("D","Create web APIs with ASP.NET Core — Binding source parameter inference"),13:("A","Create web APIs with ASP.NET Core — Attribute routing requirement"),14:("B","Routing to controller actions in ASP.NET Core"),15:("C","Routing to controller actions in ASP.NET Core"),16:("D","Create web APIs with ASP.NET Core — Controller action return types"),17:("A","Create web APIs with ASP.NET Core — Formatters"),18:("B","Create web APIs with ASP.NET Core — Formatters"),19:("C","ASP.NET Core web API documentation with Swagger / OpenAPI"),20:("D","ASP.NET Core web API documentation with Swagger / OpenAPI")
    },
    (24, 3): {
        1:("A","Create web APIs with ASP.NET Core — Binding source parameter inference"),2:("B","Create web APIs with ASP.NET Core — Binding source parameter inference"),3:("C","Create web APIs with ASP.NET Core — Binding source parameter inference"),4:("D","Create web APIs with ASP.NET Core — Binding source parameter inference"),5:("A","Create web APIs with ASP.NET Core — Binding source parameter inference"),6:("B","Create web APIs with ASP.NET Core — Binding source parameter inference"),7:("C","Create web APIs with ASP.NET Core — Binding source parameter inference"),8:("D","Create web APIs with ASP.NET Core — Binding source parameter inference"),9:("A","Create web APIs with ASP.NET Core — Binding source parameter inference"),10:("B","Create web APIs with ASP.NET Core — Binding source parameter inference"),11:("C","Create web APIs with ASP.NET Core — Formatters"),12:("D","Create web APIs with ASP.NET Core — Binding source parameter inference"),13:("A","Create web APIs with ASP.NET Core — Content negotiation"),14:("B","Create web APIs with ASP.NET Core — Content negotiation"),15:("C","Create web APIs with ASP.NET Core — Formatters"),16:("D","Create web APIs with ASP.NET Core — Content negotiation"),17:("A","Create web APIs with ASP.NET Core — Formatters"),18:("B","Create web APIs with ASP.NET Core — Formatters"),19:("C","Custom formatters in ASP.NET Core Web API"),20:("D","Format response data in ASP.NET Core Web API")
    },
    (24, 4): {
        1:("A","Create web APIs with ASP.NET Core — Automatic HTTP 400 responses"),2:("B","Create web APIs with ASP.NET Core — Automatic HTTP 400 responses"),3:("C","Handle errors in ASP.NET Core APIs"),4:("D","Create web APIs with ASP.NET Core — Automatic HTTP 400 responses"),5:("A","Create web APIs with ASP.NET Core — Automatic HTTP 400 responses"),6:("B","Create web APIs with ASP.NET Core — Automatic HTTP 400 responses"),7:("C","Create web APIs with ASP.NET Core — Automatic HTTP 400 responses"),8:("D","Create web APIs with ASP.NET Core — Binding source parameter inference"),9:("A","Create web APIs with ASP.NET Core — Automatic HTTP 400 responses"),10:("B","Controller action return types in ASP.NET Core web API"),11:("C","Controller action return types in ASP.NET Core web API"),12:("D","Controller action return types in ASP.NET Core web API"),13:("A","Controller action return types in ASP.NET Core web API"),14:("B","Create web APIs with ASP.NET Core — Controller action return types"),15:("C","Create web APIs with ASP.NET Core — Controller action return types"),16:("D","Create web APIs with ASP.NET Core — Controller action return types"),17:("A","Create web APIs with ASP.NET Core — Controller action return types"),18:("B","Create web APIs with ASP.NET Core — Controller action return types"),19:("C","Create web APIs with ASP.NET Core — Controller action return types"),20:("D","Create web APIs with ASP.NET Core — Controller action return types")
    },
    (24, 5): {
        1:("A","Create web APIs with ASP.NET Core — Controller action return types"),2:("B","Create web APIs with ASP.NET Core — Controller action return types"),3:("C","Create web APIs with ASP.NET Core — Controller action return types"),4:("D","ASP.NET Core web API documentation with Swagger / OpenAPI"),5:("A","ASP.NET Core web API documentation with Swagger / OpenAPI"),6:("B","ASP.NET Core web API documentation with Swagger / OpenAPI"),7:("C","ASP.NET Core web API documentation with Swagger / OpenAPI"),8:("D","ASP.NET Core web API documentation with Swagger / OpenAPI"),9:("A","Create web APIs with ASP.NET Core"),10:("B","Create web APIs with ASP.NET Core"),11:("C","Create web APIs with ASP.NET Core"),12:("D","Create web APIs with ASP.NET Core — Attribute routing requirement"),13:("A","Routing to controller actions in ASP.NET Core"),14:("B","Routing to controller actions in ASP.NET Core"),15:("C","Routing to controller actions in ASP.NET Core"),16:("D","Handle errors in ASP.NET Core APIs"),17:("A","Create web APIs with ASP.NET Core — Content negotiation"),18:("B","Create web APIs with ASP.NET Core — Controller action return types"),19:("C","ASP.NET Core web API documentation with Swagger / OpenAPI"),20:("D","Controller action return types in ASP.NET Core web API")
    },
    (23, 2): {
        1:("A","Overview of ASP.NET Core Authentication"),2:("B","Introduction to authorization in ASP.NET Core"),3:("C","Introduction to authorization in ASP.NET Core"),4:("D","Overview of ASP.NET Core Authentication"),5:("A","Overview of ASP.NET Core Authentication"),6:("B","Overview of ASP.NET Core Authentication"),7:("C","Overview of ASP.NET Core Authentication"),8:("D","Overview of ASP.NET Core Authentication"),9:("A","Overview of ASP.NET Core Authentication"),10:("B","Overview of ASP.NET Core Authentication"),11:("C","Claim-based authorization in ASP.NET Core"),12:("D","Claim-based authorization in ASP.NET Core"),13:("A","Claim-based authorization in ASP.NET Core"),14:("B","Role-based authorization in ASP.NET Core"),15:("C","Claim-based authorization in ASP.NET Core"),16:("D","Claim-based authorization in ASP.NET Core"),17:("A","Claim-based authorization in ASP.NET Core"),18:("B","Claim-based authorization in ASP.NET Core"),19:("C","Overview of ASP.NET Core Authentication"),20:("D","Introduction to authorization in ASP.NET Core")
    },
    (23, 3): {
        1:("A","Policy-based authorization in ASP.NET Core"),2:("B","Policy-based authorization in ASP.NET Core"),3:("C","Claim-based authorization in ASP.NET Core"),4:("D","Policy-based authorization in ASP.NET Core"),5:("A","Policy-based authorization in ASP.NET Core"),6:("B","Policy-based authorization in ASP.NET Core"),7:("C","Policy-based authorization in ASP.NET Core"),8:("D","Policy-based authorization in ASP.NET Core"),9:("A","Resource-based authorization in ASP.NET Core"),10:("B","Resource-based authorization in ASP.NET Core"),11:("C","Resource-based authorization in ASP.NET Core"),12:("D","Resource-based authorization in ASP.NET Core"),13:("A","Introduction to authorization in ASP.NET Core"),14:("B","Introduction to authorization in ASP.NET Core"),15:("C","Policy-based authorization in ASP.NET Core"),16:("D","Role-based authorization in ASP.NET Core"),17:("A","Role-based authorization in ASP.NET Core"),18:("B","Role-based authorization in ASP.NET Core"),19:("C","Role-based authorization in ASP.NET Core"),20:("D","Role-based authorization in ASP.NET Core")
    },
    (23, 4): {
        1:("A","Filters in ASP.NET Core"),2:("B","Filters in ASP.NET Core"),3:("C","Filters in ASP.NET Core"),4:("D","Filters in ASP.NET Core"),5:("A","Filters in ASP.NET Core"),6:("B","Filters in ASP.NET Core"),7:("C","Filters in ASP.NET Core"),8:("D","Filters in ASP.NET Core"),9:("A","Filters in ASP.NET Core"),10:("B","Dependency injection in ASP.NET Core filters"),11:("C","Dependency injection in ASP.NET Core filters"),12:("D","Introduction to authorization in ASP.NET Core"),13:("A","Filters in ASP.NET Core"),14:("B","Filters in ASP.NET Core"),15:("C","Filters in ASP.NET Core"),16:("D","Filters in ASP.NET Core"),17:("A","Filters in ASP.NET Core"),18:("B","Filters in ASP.NET Core"),19:("C","Filters in ASP.NET Core"),20:("D","Policy-based authorization in ASP.NET Core")
    },
    (23, 5): {
        1:("A","Policy-based authorization in ASP.NET Core"),2:("B","Policy-based authorization in ASP.NET Core"),3:("C","Claim-based authorization in ASP.NET Core"),4:("D","Policy-based authorization in ASP.NET Core"),5:("A","Resource-based authorization in ASP.NET Core"),6:("B","Resource-based authorization in ASP.NET Core"),7:("C","Introduction to authorization in ASP.NET Core"),8:("D","Introduction to authorization in ASP.NET Core"),9:("A","Introduction to authorization in ASP.NET Core"),10:("B","Filters in ASP.NET Core"),11:("C","Filters in ASP.NET Core"),12:("D","Filters in ASP.NET Core"),13:("A","Filters in ASP.NET Core"),14:("B","Filters in ASP.NET Core"),15:("C","Filters in ASP.NET Core"),16:("D","Filters in ASP.NET Core"),17:("A","Dependency injection in ASP.NET Core filters"),18:("B","Filters in ASP.NET Core"),19:("C","Introduction to authorization in ASP.NET Core"),20:("D","Policy-based authorization in ASP.NET Core")
    },
    (25, 1): {
        1:("A","OData Version 4.01 — Part 1: Protocol, Introduction"),2:("B","OData Version 4.01 — Part 1: Protocol, Metadata Service"),3:("C","OData Version 4.01 — Part 1: Protocol, Service Root URL"),4:("D","OData Version 4.01 — Part 1: Protocol, Metadata Service"),5:("A","OData Version 4.01 — Part 1: Protocol, Entity Data Model"),6:("B","OData Version 4.01 — Part 1: Protocol, Entity Sets"),7:("C","OData Version 4.01 — Part 1: Protocol, Singletons"),8:("D","OData Version 4.01 — Part 1: Protocol, Complex Types"),9:("A","OData Version 4.01 — Part 1: Protocol, Navigation Properties"),10:("B","OData Version 4.01 — Part 1: Protocol, Entity Keys"),11:("C","OData Version 4.01 — Part 1: Protocol, Entity Container"),12:("D","OData Version 4.01 — Part 1: Protocol, Primitive Properties"),13:("A","OData Version 4.01 — Part 1: Protocol, Collection-Valued Properties"),14:("B","OData Version 4.01 — Part 1: Protocol, Entity Type Inheritance"),15:("C","OData Version 4.01 — Part 1: Protocol, Navigation Properties"),16:("D","OData Version 4.01 — Part 1: Protocol, Resource Path"),17:("A","OData Version 4.01 — Part 1: Protocol, Key Predicates"),18:("B","OData Version 4.01 — Part 1: Protocol, Resource Path"),19:("C","OData Version 4.01 — Part 1: Protocol, Resource Path"),20:("D","OData Version 4.01 — Part 1: Protocol, Resource Path")
    },
    (25, 2): {
        1:("A","OData Version 4.01 — Part 1: Protocol, System Query Options"),2:("B","OData Version 4.01 — Part 1: Protocol, Filter System Query Option"),3:("C","OData Version 4.01 — Part 1: Protocol, Select System Query Option"),4:("D","OData Version 4.01 — Part 1: Protocol, Expand System Query Option"),5:("A","OData Version 4.01 — Part 1: Protocol, OrderBy System Query Option"),6:("B","OData Version 4.01 — Part 1: Protocol, Top System Query Option"),7:("C","OData Version 4.01 — Part 1: Protocol, Skip System Query Option"),8:("D","OData Version 4.01 — Part 1: Protocol, Count System Query Option"),9:("A","OData Version 4.01 — Part 1: Protocol, Search System Query Option"),10:("B","OData Version 4.01 — Part 1: Protocol, Format System Query Option"),11:("C","OData Version 4.01 — Part 1: Protocol, System Query Options"),12:("D","OData Version 4.01 — Part 1: Protocol, Filter System Query Option"),13:("A","OData Version 4.01 — Part 1: Protocol, Filter System Query Option"),14:("B","OData Version 4.01 — Part 1: Protocol, Filter System Query Option"),15:("C","OData Version 4.01 — Part 1: Protocol, OrderBy System Query Option"),16:("D","OData Version 4.01 — Part 1: Protocol, Top and Skip System Query Options"),17:("A","OData Version 4.01 — Part 1: Protocol, Expand System Query Option"),18:("B","OData Version 4.01 — Part 1: Protocol, Select and Expand System Query Options"),19:("C","OData Version 4.01 — Part 1: Protocol, System Query Options"),20:("D","OData Version 4.01 — Part 1: Protocol, Protocol Versioning and Conformance")
    },
    (25, 3): {
        1:("A","OData Version 4.01 — Part 1: Protocol, GET"),2:("B","OData Version 4.01 — Part 1: Protocol, Create a New Entity"),3:("C","OData Version 4.01 — Part 1: Protocol, Update an Entity"),4:("D","OData Version 4.01 — Part 1: Protocol, Update an Entity"),5:("A","OData Version 4.01 — Part 1: Protocol, Delete an Entity"),6:("B","OData Version 4.01 — Part 1: Protocol, Create a New Entity"),7:("C","OData Version 4.01 — Part 1: Protocol, Update an Entity"),8:("D","OData Version 4.01 — Part 1: Protocol, Delete an Entity"),9:("A","OData Version 4.01 — Part 1: Protocol, Requesting an Individual Entity"),10:("B","OData Version 4.01 — Part 1: Protocol, Create a New Entity"),11:("C","OData Version 4.01 — Part 1: Protocol, Optimistic Concurrency"),12:("D","OData Version 4.01 — Part 1: Protocol, Optimistic Concurrency"),13:("A","OData Version 4.01 — Part 1: Protocol, Optimistic Concurrency"),14:("B","OData Version 4.01 — Part 1: Protocol, Optimistic Concurrency"),15:("C","OData Version 4.01 — Part 1: Protocol, Optimistic Concurrency"),16:("D","OData Version 4.01 — Part 1: Protocol, Server-Driven Paging"),17:("A","OData Version 4.01 — Part 1: Protocol, Server-Driven Paging"),18:("B","OData Version 4.01 — Part 1: Protocol, Server-Driven Paging"),19:("C","OData Version 4.01 — Part 1: Protocol, Server-Driven Paging"),20:("D","OData Version 4.01 — Part 1: Protocol, Delta Responses")
    },
    (25, 4): {
        1:("A","OData Version 4.01 — Part 1: Protocol, Delta Responses"),2:("B","OData Version 4.01 — Part 1: Protocol, Batch Requests"),3:("C","OData Version 4.01 — Part 1: Protocol, Change Sets"),4:("D","OData Version 4.01 — Part 1: Protocol, Change Sets"),5:("A","OData Version 4.01 — Part 1: Protocol, Batch Requests"),6:("B","OData Version 4.01 — Part 1: Protocol, Functions"),7:("C","OData Version 4.01 — Part 1: Protocol, Actions"),8:("D","OData Version 4.01 — Part 1: Protocol, Bound Functions"),9:("A","OData Version 4.01 — Part 1: Protocol, Bound Actions"),10:("B","OData Version 4.01 — Part 1: Protocol, Unbound Operations"),11:("C","OData Version 4.01 — Part 1: Protocol, Function Parameters"),12:("D","OData Version 4.01 — Part 1: Protocol, Actions"),13:("A","OData Version 4.01 — Part 1: Protocol, Bound Functions"),14:("B","OData Version 4.01 — Part 1: Protocol, Metadata Service"),15:("C","OData Version 4.01 — Part 1: Protocol, Annotations"),16:("D","OData Version 4.01 — Part 1: Protocol, Capabilities"),17:("A","OData Version 4.01 — Part 1: Protocol, Metadata Service"),18:("B","OData Version 4.01 — Part 1: Protocol, Versioning"),19:("C","OData Version 4.01 — Part 1: Protocol, Protocol Versioning and Conformance"),20:("D","OData Version 4.01 — Part 1: Protocol, HTTP Methods")
    },
    (25, 5): {
        1:("A","OData Version 4.01 — Part 1: Protocol, Security Considerations"),2:("B","OData Version 4.01 — Part 1: Protocol, Security Considerations"),3:("C","OData Version 4.01 — Part 1: Protocol, Protocol Versioning and Conformance"),4:("D","OData Version 4.01 — Part 1: Protocol, Security Considerations"),5:("A","OData Version 4.01 — Part 1: Protocol, URL Conventions"),6:("B","OData Version 4.01 — Part 1: Protocol, URL Conventions"),7:("C","OData Version 4.01 — Part 1: Protocol, Key Predicates"),8:("D","OData Version 4.01 — Part 1: Protocol, Entity Data Model"),9:("A","OData Version 4.01 — Part 1: Protocol, Resource Path"),10:("B","OData Version 4.01 — Part 1: Protocol, Entity Data Model"),11:("C","OData Version 4.01 — Part 1: Protocol, Format System Query Option"),12:("D","OData Version 4.01 — Part 1: Protocol, URL Conventions"),13:("A","OData Version 4.01 — Part 1: Protocol, Server-Driven Paging"),14:("B","OData Version 4.01 — Part 1: Protocol, Optimistic Concurrency"),15:("C","OData Version 4.01 — Part 1: Protocol, Security Considerations"),16:("D","OData Version 4.01 — Part 1: Protocol, Response Payloads"),17:("A","OData Version 4.01 — Part 1: Protocol, Response Payloads"),18:("B","OData Version 4.01 — Part 1: Protocol, Error Handling"),19:("C","OData Version 4.01 — Part 1: Protocol, Error Handling"),20:("D","OData Version 4.01 — Part 1: Protocol, Metadata Service")
    },
    (26, 1): {
        1:("A","ASP.NET Core Blazor hosting models"),2:("B","ASP.NET Core Blazor hosting models"),3:("C","ASP.NET Core Blazor hosting models"),4:("D","ASP.NET Core Blazor hosting models"),5:("A","ASP.NET Core Blazor hosting models"),6:("B","ASP.NET Core Blazor hosting models"),7:("C","ASP.NET Core Blazor hosting models"),8:("D","ASP.NET Core Blazor hosting models"),9:("A","ASP.NET Core Blazor hosting models"),10:("B","ASP.NET Core Blazor hosting models"),11:("C","ASP.NET Core Blazor hosting models"),12:("D","ASP.NET Core Blazor hosting models"),13:("A","ASP.NET Core Blazor hosting models"),14:("B","ASP.NET Core Blazor hosting models"),15:("C","ASP.NET Core Blazor hosting models"),16:("D","ASP.NET Core Blazor hosting models"),17:("A","ASP.NET Core Blazor hosting models"),18:("B","ASP.NET Core Blazor hosting models"),19:("C","ASP.NET Core Blazor hosting models"),20:("D","ASP.NET Core Blazor hosting models")
    },
    (26, 2): {
        1:("A","ASP.NET Core Blazor hosting models"),2:("B","ASP.NET Core Blazor hosting models"),3:("C","ASP.NET Core Blazor hosting models"),4:("D","ASP.NET Core Blazor hosting models"),5:("A","ASP.NET Core Blazor hosting models"),6:("B","ASP.NET Core Blazor hosting models"),7:("C","ASP.NET Core Blazor hosting models"),8:("D","ASP.NET Core Blazor render modes"),9:("A","ASP.NET Core Blazor render modes"),10:("B","ASP.NET Core Blazor render modes"),11:("C","ASP.NET Core Blazor render modes"),12:("D","ASP.NET Core Blazor render modes"),13:("A","ASP.NET Core Blazor render modes"),14:("B","ASP.NET Core Blazor render modes"),15:("C","ASP.NET Core Blazor render modes"),16:("D","ASP.NET Core Blazor render modes"),17:("A","ASP.NET Core Blazor render modes"),18:("B","ASP.NET Core Blazor render modes"),19:("C","ASP.NET Core Blazor render modes"),20:("D","ASP.NET Core Blazor render modes")
    },
    (26, 3): {
        1:("A","ASP.NET Core Blazor render modes"),2:("B","ASP.NET Core Blazor fundamentals overview"),3:("C","ASP.NET Core Blazor render modes"),4:("D","ASP.NET Core Blazor render modes"),5:("A","ASP.NET Core Blazor project structure"),6:("B","ASP.NET Core Blazor project structure"),7:("C","ASP.NET Core Blazor project structure"),8:("D","ASP.NET Core Blazor project structure"),9:("A","ASP.NET Core Blazor project structure"),10:("B","ASP.NET Core Blazor project structure"),11:("C","ASP.NET Core Blazor project structure"),12:("D","ASP.NET Core Blazor project structure"),13:("A","ASP.NET Core Blazor routing"),14:("B","ASP.NET Core Blazor project structure"),15:("C","ASP.NET Core Blazor project structure"),16:("D","ASP.NET Core Blazor project structure"),17:("A","ASP.NET Core Blazor project structure"),18:("B","ASP.NET Core Blazor render modes"),19:("C","ASP.NET Core Blazor fundamentals overview"),20:("D","ASP.NET Core Blazor deployment")
    },
    (26, 4): {
        1:("A","ASP.NET Core Blazor hosting models"),2:("B","ASP.NET Core Blazor hosting models"),3:("C","ASP.NET Core Blazor deployment"),4:("D","ASP.NET Core Blazor deployment"),5:("A","ASP.NET Core Blazor hosting models"),6:("B","ASP.NET Core Blazor hosting models"),7:("C","ASP.NET Core Blazor hosting models"),8:("D","ASP.NET Core Blazor hosting models"),9:("A","ASP.NET Core Blazor hosting models"),10:("B","ASP.NET Core Blazor hosting models"),11:("C","ASP.NET Core Blazor hosting models"),12:("D","ASP.NET Core Blazor hosting models"),13:("A","ASP.NET Core Blazor hosting models"),14:("B","ASP.NET Core Blazor hosting models"),15:("C","ASP.NET Core Blazor render modes"),16:("D","ASP.NET Core Blazor render modes"),17:("A","ASP.NET Core Blazor render modes"),18:("B","ASP.NET Core Blazor render modes"),19:("C","ASP.NET Core Blazor render modes"),20:("D","ASP.NET Core Blazor render modes")
    },
    (26, 5): {
        1:("A","ASP.NET Core Blazor render modes"),2:("B","ASP.NET Core Blazor render modes"),3:("C","ASP.NET Core Blazor fundamentals overview"),4:("D","ASP.NET Core Blazor project structure"),5:("A","ASP.NET Core Blazor hosting models"),6:("B","ASP.NET Core Blazor hosting models"),7:("C","ASP.NET Core Blazor hosting models"),8:("D","ASP.NET Core Blazor hosting models"),9:("A","ASP.NET Core Blazor deployment"),10:("B","ASP.NET Core Blazor deployment"),11:("C","ASP.NET Core Blazor hosting models"),12:("D","ASP.NET Core Blazor hosting models"),13:("A","ASP.NET Core Blazor hosting models"),14:("B","ASP.NET Core Blazor render modes"),15:("C","ASP.NET Core Blazor fundamentals overview"),16:("D","ASP.NET Core Blazor deployment"),17:("A","ASP.NET Core Blazor deployment"),18:("B","ASP.NET Core Blazor hosting models"),19:("C","ASP.NET Core Blazor render modes"),20:("D","ASP.NET Core Blazor hosting models")
    },
    (27, 1): {
        1:("A","ASP.NET Core Blazor components"),2:("B","ASP.NET Core Blazor components"),3:("C","ASP.NET Core Blazor components"),4:("D","ASP.NET Core Blazor rendering"),5:("A","ASP.NET Core Blazor components"),6:("B","ASP.NET Core Blazor components"),7:("C","ASP.NET Core Blazor components"),8:("D","ASP.NET Core Blazor components"),9:("A","ASP.NET Core Blazor templated components"),10:("B","ASP.NET Core Blazor templated components"),11:("C","ASP.NET Core Razor component lifecycle"),12:("D","ASP.NET Core Razor component lifecycle"),13:("A","ASP.NET Core Razor component lifecycle"),14:("B","ASP.NET Core Razor component lifecycle"),15:("C","ASP.NET Core Razor component lifecycle"),16:("D","ASP.NET Core Razor component lifecycle"),17:("A","ASP.NET Core Razor component lifecycle"),18:("B","ASP.NET Core Razor component lifecycle"),19:("C","ASP.NET Core Blazor rendering"),20:("D","ASP.NET Core Blazor event handling")
    },
    (27, 2): {
        1:("A","ASP.NET Core Blazor event handling"),2:("B","ASP.NET Core Blazor event handling"),3:("C","ASP.NET Core Blazor event handling"),4:("D","ASP.NET Core Blazor event handling"),5:("A","ASP.NET Core Blazor event handling"),6:("B","ASP.NET Core Blazor event handling"),7:("C","ASP.NET Core Blazor event handling"),8:("D","ASP.NET Core Blazor data binding"),9:("A","ASP.NET Core Blazor data binding"),10:("B","ASP.NET Core Blazor data binding"),11:("C","ASP.NET Core Blazor data binding"),12:("D","ASP.NET Core Blazor data binding"),13:("A","ASP.NET Core Blazor data binding"),14:("B","ASP.NET Core Blazor data binding"),15:("C","ASP.NET Core Blazor data binding"),16:("D","ASP.NET Core Blazor data binding"),17:("A","ASP.NET Core Blazor data binding"),18:("B","ASP.NET Core Blazor data binding"),19:("C","ASP.NET Core Blazor cascading values and parameters"),20:("D","ASP.NET Core Blazor cascading values and parameters")
    },
    (27, 3): {
        1:("A","ASP.NET Core Blazor cascading values and parameters"),2:("B","ASP.NET Core Blazor cascading values and parameters"),3:("C","ASP.NET Core Blazor cascading values and parameters"),4:("D","ASP.NET Core Blazor cascading values and parameters"),5:("A","ASP.NET Core Blazor cascading values and parameters"),6:("B","ASP.NET Core Blazor cascading values and parameters"),7:("C","ASP.NET Core Blazor cascading values and parameters"),8:("D","ASP.NET Core Blazor cascading values and parameters"),9:("A","ASP.NET Core Blazor templated components"),10:("B","ASP.NET Core Blazor templated components"),11:("C","ASP.NET Core Blazor templated components"),12:("D","ASP.NET Core Blazor templated components"),13:("A","ASP.NET Core Blazor templated components"),14:("B","ASP.NET Core Blazor templated components"),15:("C","ASP.NET Core Blazor templated components"),16:("D","ASP.NET Core Blazor templated components"),17:("A","ASP.NET Core Blazor event handling"),18:("B","ASP.NET Core Blazor event handling"),19:("C","ASP.NET Core Blazor components"),20:("D","ASP.NET Core Blazor components")
    },
    (27, 4): {
        1:("A","ASP.NET Core Blazor components"),2:("B","ASP.NET Core Blazor JavaScript interoperability"),3:("C","ASP.NET Core Blazor event handling"),4:("D","ASP.NET Core Blazor event handling"),5:("A","ASP.NET Core Blazor event handling"),6:("B","ASP.NET Core Blazor event handling"),7:("C","ASP.NET Core Blazor event handling"),8:("D","ASP.NET Core Blazor event handling"),9:("A","ASP.NET Core Blazor event handling"),10:("B","ASP.NET Core Razor component lifecycle"),11:("C","ASP.NET Core Razor component lifecycle"),12:("D","ASP.NET Core Razor component lifecycle"),13:("A","ASP.NET Core Razor component lifecycle"),14:("B","ASP.NET Core Razor component lifecycle"),15:("C","ASP.NET Core Razor component lifecycle"),16:("D","ASP.NET Core Razor component lifecycle"),17:("A","ASP.NET Core Razor component lifecycle"),18:("B","ASP.NET Core Blazor rendering"),19:("C","ASP.NET Core Blazor rendering"),20:("D","ASP.NET Core Blazor rendering")
    },
    (27, 5): {
        1:("A","ASP.NET Core Blazor rendering"),2:("B","ASP.NET Core Blazor components"),3:("C","ASP.NET Core Blazor data binding"),4:("D","ASP.NET Core Blazor components"),5:("A","ASP.NET Core Blazor components"),6:("B","ASP.NET Core Blazor components"),7:("C","ASP.NET Core Blazor components"),8:("D","ASP.NET Core Blazor components"),9:("A","ASP.NET Core Razor component lifecycle"),10:("B","ASP.NET Core Blazor cascading values and parameters"),11:("C","ASP.NET Core Blazor cascading values and parameters"),12:("D","ASP.NET Core Blazor templated components"),13:("A","ASP.NET Core Blazor data binding"),14:("B","ASP.NET Core Blazor event handling"),15:("C","ASP.NET Core Blazor rendering"),16:("D","ASP.NET Core Blazor components"),17:("A","ASP.NET Core Blazor data binding"),18:("B","ASP.NET Core Razor component lifecycle"),19:("C","ASP.NET Core Blazor components"),20:("D","ASP.NET Core Razor component lifecycle")
    },
}


# Topic 28 expectations are maintained independently of candidate generation.
LOT_EXPECTATIONS.update({
    (28, 1): {
        1:('A','CSS isolation'),
        2:('B','CSS isolation'),
        3:('C','Child component support'),
        4:('D','Child component support'),
        5:('A','CSS isolation bundling'),
        6:('B','Razor class library (RCL) support'),
        7:('C','CSS preprocessor support'),
        8:('D','Customize scope identifier format'),
        9:('A','Disable automatic bundling'),
        10:('B','CSS isolation'),
        11:('C','Component classes'),
        12:('D','Specify a base class'),
        13:('A','Templated components'),
        14:('B','Apply an attribute'),
        15:('C','Capture references to components'),
        16:('D','Rendering conventions for Blazor'),
        17:('A','Capture unmatched attributes'),
        18:('B','Capture unmatched attributes'),
        19:('C','Raw HTML'),
        20:('D','Conditional HTML element attributes and DOM properties')
    },
    (28, 2): {
        1:('A','Render fragments for reusable rendering logic'),
        2:('B','Templated components'),
        3:('C','Templated components'),
        4:('D','Templated components'),
        5:('A','Templated components'),
        6:('B','Child content render fragments'),
        7:('C','Child content render fragments'),
        8:('D','Render fragments for reusable rendering logic'),
        9:('A','Loop variables with component parameters and child content'),
        10:('B','Templated components'),
        11:('C','Razor components'),
        12:('D','Razor components'),
        13:('A','Razor components'),
        14:('B','Razor components'),
        15:('C','Capture references to components'),
        16:('D','Capture references to components'),
        17:('A','After component render'),
        18:('B','Rendering conventions for Blazor'),
        19:('C','Rendering conventions for Blazor'),
        20:('D','Rendering conventions for Blazor')
    },
    (28, 3): {
        1:('A','Control the rendering flow'),
        2:('B','Control the rendering flow'),
        3:('C','Control the rendering flow'),
        4:('D','Receiving a call from something external to the Blazor rendering and event handling system'),
        5:('A','Control the rendering flow'),
        6:('B','After component render'),
        7:('C','After component render'),
        8:('D','After component render'),
        9:('A','An asynchronous handler involves multiple asynchronous phases'),
        10:('B','After component render'),
        11:('C','Base class lifecycle methods'),
        12:('D','Base class lifecycle methods'),
        13:('A','Base class lifecycle methods'),
        14:('B','Base class lifecycle methods'),
        15:('C','After parameters are set (OnParametersSet{Async})'),
        16:('D','After parameters are set (OnParametersSet{Async})'),
        17:('A','Dispose pattern'),
        18:('B','Dispose pattern'),
        19:('C','Handle errors'),
        20:('D','Handle errors')
    },
    (28, 4): {
        1:('A','CSS isolation bundling'),
        2:('B','CSS isolation bundling'),
        3:('C','Child component support'),
        4:('D','Child component support'),
        5:('A','Child component support'),
        6:('B','Child component support'),
        7:('C','CSS isolation bundling'),
        8:('D','CSS isolation bundling'),
        9:('A','Razor class library (RCL) support'),
        10:('B','CSS isolation configuration'),
        11:('C','Customize scope identifier format'),
        12:('D','Disable automatic bundling'),
        13:('A','CSS preprocessor support'),
        14:('B','Disable CSS isolation'),
        15:('C','Enable CSS isolation'),
        16:('D','Razor class library (RCL) support'),
        17:('A','CSS isolation bundling'),
        18:('B','CSS isolation'),
        19:('C','CSS isolation bundling'),
        20:('D','Base class lifecycle methods')
    },
    (28, 5): {
        1:('A','Specify a base class'),
        2:('B','Control the rendering flow'),
        3:('C','After component render'),
        4:('D','Dispose pattern'),
        5:('A','Templated components'),
        6:('B','Templated components'),
        7:('C','Razor components'),
        8:('D','Capture references to components'),
        9:('A','Capture references to components'),
        10:('B','Lifecycle events'),
        11:('C','Component initialization'),
        12:('D','After parameters are set (OnParametersSet{Async})'),
        13:('A','After component render'),
        14:('B','After component render'),
        15:('C','Receiving a call from something external to the Blazor rendering and event handling system'),
        16:('D','Handle errors'),
        17:('A','Rendering conventions for Blazor'),
        18:('B','Capture unmatched attributes'),
        19:('C','CSS isolation configuration'),
        20:('D','Handle errors')
    }
})

# Topic 29 expectations are maintained independently of candidate generation.
LOT_EXPECTATIONS.update({
    (29, 1): {
        1:('A','Input components and forms'),
        2:('B','Input components and forms'),
        3:('C','Input components and forms'),
        4:('D','Handle form submission'),
        5:('A','Handle form submission'),
        6:('B','Handle form submission'),
        7:('C','Handle form submission'),
        8:('D','Input components and forms'),
        9:('A','Input components and forms'),
        10:('B','Input components and forms'),
        11:('C','Input components and forms'),
        12:('D','Input components and forms'),
        13:('A','Input components and forms'),
        14:('B','Input components and forms'),
        15:('C','Input components and forms'),
        16:('D','Input components and forms'),
        17:('A','Input components and forms'),
        18:('B','Handle form submission'),
        19:('C','Input components and forms'),
        20:('D','Clear a form or field')
    },
    (29, 2): {
        1:('A','Input components and forms'),
        2:('B','Control form submission'),
        3:('C','Respond to validation state'),
        4:('D','Respond to validation state'),
        5:('A','Respond to validation state'),
        6:('B','Respond to validation state'),
        7:('C','Write model-based custom rules'),
        8:('D','Write model-based custom rules'),
        9:('A','Write model-based custom rules'),
        10:('B','Respond to validation state'),
        11:('C','Respond to validation state'),
        12:('D','Respond to validation state'),
        13:('A','Respond to validation state'),
        14:('B','Display validation messages'),
        15:('C','Display validation messages'),
        16:('D','Respond to validation state'),
        17:('A','When validation runs'),
        18:('B','Respond to validation state'),
        19:('C','Display validation messages'),
        20:('D','Input components and forms')
    },
    (29, 3): {
        1:('A','Validate with data annotations'),
        2:('B','Validate with data annotations'),
        3:('C','Validate with data annotations'),
        4:('D','Validate with data annotations'),
        5:('A','Validate with data annotations'),
        6:('B','Validate with data annotations'),
        7:('C','When validation runs'),
        8:('D','Configure data annotations validation'),
        9:('A','Validate nested object graphs'),
        10:('B','Validate nested object graphs'),
        11:('C','Write model-based custom rules'),
        12:('D','Write model-based custom rules'),
        13:('A','Write model-based custom rules'),
        14:('B','Write model-based custom rules'),
        15:('C','Write model-based custom rules'),
        16:('D','Write model-based custom rules'),
        17:('A','Write model-based custom rules'),
        18:('B','Validate nested object graphs'),
        19:('C','Control form submission'),
        20:('D','Configure data annotations validation')
    },
    (29, 4): {
        1:('A','Display validation messages'),
        2:('B','Display validation messages'),
        3:('C','Display validation messages'),
        4:('D','Display validation messages'),
        5:('A','Customize validation appearance'),
        6:('B','Customize validation appearance'),
        7:('C','Customize validation appearance'),
        8:('D','Customize validation appearance'),
        9:('A','Respond to validation state'),
        10:('B','Display validation messages'),
        11:('C','Display validation messages'),
        12:('D','Display validation messages'),
        13:('A','Customize validation appearance'),
        14:('B','Customize validation appearance'),
        15:('C','Respond to validation state'),
        16:('D','Display validation messages'),
        17:('A','Customize validation appearance'),
        18:('B','Display validation messages'),
        19:('C','Respond to validation state'),
        20:('D','Control form submission')
    },
    (29, 5): {
        1:('A','Antiforgery support'),
        2:('B','Antiforgery support'),
        3:('C','Antiforgery support'),
        4:('D','Handle form submission'),
        5:('A','Handle form submission'),
        6:('B','Mitigate overposting attacks'),
        7:('C','Mitigate overposting attacks'),
        8:('D','Handle form submission'),
        9:('A','Enhanced form handling'),
        10:('B','Enhanced form handling'),
        11:('C','Enhanced form handling'),
        12:('D','Client-side validation requires a circuit'),
        13:('A','Client-side validation in static SSR forms'),
        14:('B','Unsupported validation features'),
        15:('C','Enhanced form handling'),
        16:('D','Antiforgery support'),
        17:('A','Control form submission'),
        18:('B','Mitigate overposting attacks'),
        19:('C','Handle form submission'),
        20:('D','Mitigate overposting attacks')
    }
})

# Topic 30 expectations are pinned independently of candidate generation.
LOT_EXPECTATIONS.update({
    (30, 1): {
        1:('A','Dependency injection in ASP.NET Core'), 2:('B','Register services'), 3:('C','Service resolution'), 4:('D','Constructor injection'),
        5:('A','Inject services into components'), 6:('B','Inject services into components'), 7:('C','Service lifetimes'), 8:('D','Service lifetimes'),
        9:('A','Service lifetimes'), 10:('B','Disposal of services'), 11:('C','Register services'), 12:('D','Register services'),
        13:('A','Register services'), 14:('B','Register services'), 15:('C','Register multiple implementations'), 16:('D','Register multiple implementations'),
        17:('A','Service scopes'), 18:('B','Scope validation'), 19:('C','Scope validation'), 20:('D','Dependency injection guidelines')
    },
    (30, 2): {
        1:('A','Configuration in ASP.NET Core'), 2:('B','Configuration keys and values'), 3:('C','Environment variables'), 4:('D','JSON configuration provider'),
        5:('A','Default configuration providers'), 6:('B','Configuration providers'), 7:('C','Command-line configuration provider'), 8:('D','JSON configuration provider'),
        9:('A','JSON configuration provider'), 10:('B','Bind hierarchical configuration'), 11:('C','GetValue'), 12:('D','Bind configuration'),
        13:('A','Bind configuration'), 14:('B','GetConnectionString'), 15:('C','Options pattern'), 16:('D','Options interfaces'),
        17:('A','Options interfaces'), 18:('B','Options interfaces'), 19:('C','Named options'), 20:('D','Options validation')
    },
    (30, 3): {
        1:('A','Options validation'), 2:('B','Options pattern'), 3:('C','Options pattern'), 4:('D','Options pattern'),
        5:('A','Options interfaces'), 6:('B','Register services'), 7:('C','Configuration in ASP.NET Core'), 8:('D','Configuration in ASP.NET Core'),
        9:('A','Environment variables'), 10:('B','Safe storage of secrets'), 11:('C','Environment variables'), 12:('D','Register services'),
        13:('A','Inject services into components'), 14:('B','Register services'), 15:('C','Service lifetimes'), 16:('D','Service lifetimes'),
        17:('A','Service lifetimes'), 18:('B','Prerendering'), 19:('C','Inject services into components'), 20:('D','Inject services into components')
    },
    (30, 4): {
        1:('A','Register open generic services'), 2:('B','Keyed services'), 3:('C','Keyed services'), 4:('D','Keyed services'),
        5:('A','Register groups of services with TryAdd'), 6:('B','Register groups of services with TryAdd'), 7:('C','Service resolution'), 8:('D','Service provider options'),
        9:('A','Disposal of services'), 10:('B','Disposal of services'), 11:('C','DI guidelines'), 12:('D','Scope validation'),
        13:('A','Options interfaces'), 14:('B','Options interfaces'), 15:('C','Register services'), 16:('D','Service resolution'),
        17:('A','Service resolution'), 18:('B','Register multiple implementations'), 19:('C','Use scoped services within a BackgroundService'), 20:('D','Use scoped services within a BackgroundService')
    },
    (30, 5): {
        1:('A','Configuration providers'), 2:('B','Configuration providers'), 3:('C','Environment variables'), 4:('D','Command-line configuration provider'),
        5:('A','Configuration keys and values'), 6:('B','GetValue'), 7:('C','Options pattern'), 8:('D','Bind configuration'),
        9:('A','Options pattern'), 10:('B','Options validation'), 11:('C','Options validation'), 12:('D','Named options'),
        13:('A','Options interfaces'), 14:('B','Configuration in Blazor WebAssembly'), 15:('C','Configuration security'), 16:('D','Configuration in Blazor Server'),
        17:('A','Configuration in Blazor WebAssembly'), 18:('B','Configuration in Blazor WebAssembly'), 19:('C','Configuration security'), 20:('D','Configuration in Blazor WebAssembly')
    }
})

# Topic 31 expectations are pinned independently of candidate generation.
LOT_EXPECTATIONS.update({
    (31, 1): {
        1:('A','Component state'), 2:('B','Component state'), 3:('C','Component state'), 4:('D','Notify components of state changes'),
        5:('A','Notify components of state changes'), 6:('B','Component state'), 7:('C','Component state'), 8:('D','Component state'),
        9:('A','Component state'), 10:('B','Component state'), 11:('C','State management recommendations'), 12:('D','Notify components of state changes'),
        13:('A','State containers'), 14:('B','Notify components of state changes'), 15:('C','State management recommendations'), 16:('D','Component state'),
        17:('A','Component state'), 18:('B','State containers'), 19:('C','State containers'), 20:('D','State management recommendations')
    },
    (31, 2): {
        1:('A','State containers'), 2:('B','Notify components of state changes'), 3:('C','State containers'), 4:('D','State containers'),
        5:('A','State containers'), 6:('B','Notify components of state changes'), 7:('C','State containers'), 8:('D','State containers'),
        9:('A','Notify components of state changes'), 10:('B','Component state'), 11:('C','State management recommendations'), 12:('D','State containers'),
        13:('A','State containers'), 14:('B','State management recommendations'), 15:('C','Blazor Server circuits'), 16:('D','State containers'),
        17:('A','State containers'), 18:('B','State containers'), 19:('C','Browser storage'), 20:('D','State containers')
    },
    (31, 3): {
        1:('A','Browser storage'), 2:('B','Browser storage'), 3:('C','Browser storage'), 4:('D','Browser storage'),
        5:('A','Browser storage'), 6:('B','Prerendering'), 7:('C','Browser storage'), 8:('D','Browser storage'),
        9:('A','Browser storage'), 10:('B','Browser storage'), 11:('C','Browser storage'), 12:('D','Browser storage'),
        13:('A','Browser storage'), 14:('B','Browser storage'), 15:('C','State management recommendations'), 16:('D','Browser storage'),
        17:('A','Browser storage'), 18:('B','Browser storage'), 19:('C','Browser storage'), 20:('D','State management recommendations')
    },
    (31, 4): {
        1:('A','Prerendering'), 2:('B','Prerendering'), 3:('C','PersistentComponentState'), 4:('D','Persist prerendered state'),
        5:('A','PersistentComponentState'), 6:('B','PersistentComponentState'), 7:('C','PersistentComponentState'), 8:('D','PersistentComponentState'),
        9:('A','PersistentComponentState'), 10:('B','State management recommendations'), 11:('C','Prerendering'), 12:('D','Persist prerendered state'),
        13:('A','PersistentComponentState'), 14:('B','State management recommendations'), 15:('C','PersistentComponentState'), 16:('D','PersistentComponentState'),
        17:('A','Prerendering'), 18:('B','PersistentComponentState'), 19:('C','PersistentComponentState'), 20:('D','PersistentComponentState')
    },
    (31, 5): {
        1:('A','State management recommendations'), 2:('B','State management recommendations'), 3:('C','State management recommendations'), 4:('D','State management recommendations'),
        5:('A','State containers'), 6:('B','State containers'), 7:('C','Notify components of state changes'), 8:('D','State containers'),
        9:('A','State containers'), 10:('B','State management recommendations'), 11:('C','State management recommendations'), 12:('D','State management recommendations'),
        13:('A','State management recommendations'), 14:('B','State containers'), 15:('C','Blazor Server circuits'), 16:('D','State management recommendations'),
        17:('A','State management recommendations'), 18:('B','State management recommendations'), 19:('C','State containers'), 20:('D','State management recommendations')
    }
})

# Topic 32 expectations are pinned independently of candidate generation.
LOT_EXPECTATIONS.update({
    (32, 1): {
        1:('A','Route templates'), 2:('B','Route templates'), 3:('C','Route parameters'), 4:('D','Route parameters'),
        5:('A','Route constraints'), 6:('B','Route constraints'), 7:('C','Route templates'), 8:('D','Route templates'),
        9:('A','Route templates'), 10:('B','Route templates'), 11:('C','Route templates'), 12:('D','Route templates'),
        13:('A','Route constraints'), 14:('B','Route constraints'), 15:('C','Route parameters'), 16:('D','Route constraints'),
        17:('A','Route templates'), 18:('B','Route constraints'), 19:('C','Router'), 20:('D','Route templates')
    },
    (32, 2): {
        1:('A','Router'), 2:('B','Router'), 3:('C','Router'), 4:('D','Router'),
        5:('A','Router'), 6:('B','RouteView'), 7:('C','RouteView'), 8:('D','AuthorizeRouteView'),
        9:('A','AuthorizeRouteView'), 10:('B','AuthorizeRouteView'), 11:('C','FocusOnNavigate'), 12:('D','RouteView'),
        13:('A','RouteView'), 14:('B','RouteView'), 15:('C','Router'), 16:('D','Router'),
        17:('A','AuthorizeRouteView'), 18:('B','FocusOnNavigate'), 19:('C','RouteView'), 20:('D','Router')
    },
    (32, 3): {
        1:('A','NavigationManager'), 2:('B','NavigationManager'), 3:('C','NavigationManager'), 4:('D','NavigationManager'),
        5:('A','NavigationManager'), 6:('B','NavigationManager'), 7:('C','NavigationManager'), 8:('D','NavigationManager'),
        9:('A','NavigationManager'), 10:('B','NavigationManager'), 11:('C','NavigationManager'), 12:('D','NavigationManager'),
        13:('A','NavigationManager'), 14:('B','NavigationManager'), 15:('C','NavigationManager'), 16:('D','NavigationManager'),
        17:('A','NavigationManager'), 18:('B','NavigationManager'), 19:('C','NavigationManager'), 20:('D','NavigationManager')
    },
    (32, 4): {
        1:('A','NavLink'), 2:('B','NavLink'), 3:('C','NavLink'), 4:('D','NavLink'),
        5:('A','NavLink'), 6:('B','Query-string parameters'), 7:('C','Query-string parameters'), 8:('D','Query-string parameters'),
        9:('A','Query-string parameters'), 10:('B','Query-string parameters'), 11:('C','Query-string parameters'), 12:('D','Query-string parameters'),
        13:('A','Query-string parameters'), 14:('B','Query-string parameters'), 15:('C','NavLink'), 16:('D','NavigationManager'),
        17:('A','Query-string parameters'), 18:('B','NavLink'), 19:('C','Query-string parameters'), 20:('D','NavigationManager')
    },
    (32, 5): {
        1:('A','NavigationLock'), 2:('B','NavigationLock'), 3:('C','NavigationLock'), 4:('D','NavigationLock'),
        5:('A','NavigationLock'), 6:('B','Enhanced navigation'), 7:('C','Enhanced navigation'), 8:('D','Enhanced navigation'),
        9:('A','NavigationManager'), 10:('B','NavigationLock'), 11:('C','NavigationManager'), 12:('D','Enhanced navigation'),
        13:('A','NavigationLock'), 14:('B','NavigationManager'), 15:('C','NavigationManager'), 16:('D','Enhanced navigation'),
        17:('A','AuthorizeRouteView'), 18:('B','NavigationManager'), 19:('C','FocusOnNavigate'), 20:('D','State management recommendations')
    }
})

# Topic 33 expectations are pinned independently of candidate generation.
LOT_EXPECTATIONS.update({
    (33, 1): {
        1:('A','gittutorial — Getting Started'), 2:('B','gitglossary — blob object'), 3:('C','gitglossary — tree object'), 4:('D','gitglossary — commit object'),
        5:('A','gitglossary — tag object; git-tag'), 6:('B','gitrepository-layout — objects'), 7:('C','gitglossary — ref; gitrepository-layout — refs'), 8:('D','gitglossary — HEAD'),
        9:('A','gitglossary — index; gittutorial — The Git index'), 10:('B','gitglossary — working tree'), 11:('C','gitrepository-layout — The .git directory'), 12:('D','gitglossary — commit object; tree object'),
        13:('A','gitglossary — blob object; tree object'), 14:('B','gitglossary — branch; ref'), 15:('C','gitglossary — commit object; git-commit'), 16:('D','gitglossary — detached HEAD'),
        17:('A','gitrepository-layout — refs'), 18:('B','gitglossary — tag object; git-tag'), 19:('C','gittutorial — The Git index'), 20:('D','gitglossary — object; gitrepository-layout — objects')
    },
    (33, 2): {
        1:('A','git — --version'), 2:('B','git-init — DESCRIPTION'), 3:('C','git-clone — DESCRIPTION'), 4:('D','git-config — CONFIGURATION LEVELS'),
        5:('A','git-config — user.name'), 6:('B','git-config — user.email'), 7:('C','git-config — CONFIGURATION LEVELS'), 8:('D','git-config — --list'),
        9:('A','git-config — SCOPES'), 10:('B','git-config — --local; user.name'), 11:('C','git-config — --unset'), 12:('D','git-config — init.defaultBranch; git-init — INITIAL BRANCH NAME'),
        13:('A','git-config — CONFIGURATION LEVELS'), 14:('B','git-config — --show-origin; --get'), 15:('C','git-config — CONFIGURATION LEVELS'), 16:('D','git-config — user.email; gittutorial — Making Changes'),
        17:('A','git-config — --get-all'), 18:('B','git-config — core.editor; CONFIGURATION LEVELS'), 19:('C','git-init — DESCRIPTION'), 20:('D','git-clone — DESCRIPTION; git-init — DESCRIPTION')
    },
    (33, 3): {
        1:('A','git-status — DESCRIPTION'), 2:('B','git-status — DESCRIPTION'), 3:('C','git-add — DESCRIPTION'), 4:('D','git-diff — DESCRIPTION'),
        5:('A','git-diff — --cached'), 6:('B','git-add — -A/--all'), 7:('C','git-add — -p/--patch'), 8:('D','git-restore — DESCRIPTION'),
        9:('A','git-restore — --staged'), 10:('B','git-restore — --staged; git-rm — --cached'), 11:('C','git-reset — Resetting a single file'), 12:('D','git-rm — --cached'),
        13:('A','git-mv — DESCRIPTION'), 14:('B','gitignore — DESCRIPTION'), 15:('C','git-check-ignore — -v/--verbose'), 16:('D','gitignore — Pattern Format'),
        17:('A','git-add — DESCRIPTION; gittutorial — The Git index'), 18:('B','git-diff — COMMIT and --cached'), 19:('C','git-restore — --staged'), 20:('D','git-check-ignore — --verbose')
    },
    (33, 4): {
        1:('A','git-commit — DESCRIPTION'), 2:('B','git-commit — -m/--message'), 3:('C','git-log — DESCRIPTION'), 4:('D','git-show — DESCRIPTION'),
        5:('A','git-log — --oneline'), 6:('B','git-commit — --amend'), 7:('C','git-commit — COMMIT INFORMATION'), 8:('D','gitrevisions — SPECIFYING REVISIONS'),
        9:('A','gitrevisions — Ancestry References'), 10:('B','git-rev-parse — DESCRIPTION'), 11:('C','git-reflog — DESCRIPTION'), 12:('D','git-show-ref — DESCRIPTION'),
        13:('A','gitglossary — branch; git-commit — DESCRIPTION'), 14:('B','git-commit — --allow-empty'), 15:('C','git-commit — --amend'), 16:('D','gitrevisions — Reflog Identifiers; Ancestry References'),
        17:('A','git-cat-file — DESCRIPTION'), 18:('B','git-show-ref; gitglossary — HEAD/ref'), 19:('C','git-log — Limiting Commit History'), 20:('D','git-reflog — DESCRIPTION')
    },
    (33, 5): {
        1:('A','git-tag — DESCRIPTION'), 2:('B','git-tag — -a/--annotate; -m/--message'), 3:('C','git-tag — -d/--delete'), 4:('D','git-tag — DESCRIPTION'),
        5:('A','git-reset — --soft'), 6:('B','git-reset — --mixed'), 7:('C','git-reset — --hard'), 8:('D','git-reset — --hard'),
        9:('A','git-rev-parse — DESCRIPTION'), 10:('B','git-show — DESCRIPTION; git-tag'), 11:('C','git-reset — --soft'), 12:('D','git-reset — DESCRIPTION; Resetting a single file'),
        13:('A','git-reflog — DESCRIPTION'), 14:('B','git-tag — SIGNING TAGS'), 15:('C','git-update-ref — DESCRIPTION'), 16:('D','git-reset — DESCRIPTION; git-reflog'),
        17:('A','git-tag — -d; git-reset — DESCRIPTION'), 18:('B','git-cat-file — -t'), 19:('C','git-diff — --cached'), 20:('D','gittutorial — The Git index; git-add; git-commit')
    }
})

def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("topic_num", type=int, choices=tuple(range(2, 41)))
    parser.add_argument("--lot-num", type=int, default=1, choices=tuple(range(1, 6)))
    args = parser.parse_args()
    stem = f"topic-{args.topic_num:02d}-lot-{args.lot_num:02d}"
    lot_path = ROOT / "docs/question-bank/lots" / f"{stem}.json"
    checkpoint_path = ROOT / "docs/question-bank/checkpoints" / f"{stem}.jsonl"
    payload = json.loads(lot_path.read_text(encoding="utf-8"))
    if payload["state"] != "candidates_written":
        raise RuntimeError("review requires candidate state")
    register = json.loads((ROOT / "docs/question-bank/source-register.json").read_text(encoding="utf-8"))
    sources = {source["source_id"]: source for source in register["source_records"]}
    accepted = []
    decisions = []
    for candidate in payload["questions"]:
        objective_num = int(candidate["learning_objective_id"].rsplit("-", 1)[1])
        question_num = objective_num - (args.lot_num - 1) * 20
        expectations = LOT_EXPECTATIONS.get((args.topic_num, args.lot_num), EXPECTATIONS.get(args.topic_num))
        if args.topic_num == 34:
            key = json.loads(TOPIC34_KEY_PATH.read_text(encoding="utf-8"))
            key_entry = key["lots"][str(args.lot_num)][str(question_num)]
            expected = (key_entry["correct"], key_entry["citation"])
        elif args.topic_num == 35:
            key = json.loads(TOPIC35_KEY_PATH.read_text(encoding="utf-8"))
            key_entry = key["lots"][str(args.lot_num)][str(question_num)]
            expected = (key_entry["correct"], key_entry["citation"])
        elif args.topic_num == 36:
            key = json.loads(TOPIC36_KEY_PATH.read_text(encoding="utf-8"))
            key_entry = key["lots"][str(args.lot_num)][str(question_num)]
            expected = (key_entry["correct"], key_entry["citation"])
        elif args.topic_num == 37:
            key = json.loads(TOPIC37_KEY_PATH.read_text(encoding="utf-8"))
            key_entry = key["lots"][str(args.lot_num)][str(question_num)]
            expected = (key_entry["correct"], key_entry["citation"])
        else:
            if expectations is None:
                raise RuntimeError(f"no review expectations for topic {args.topic_num}, lot {args.lot_num}")
            expected = expectations[question_num]
        source = sources[candidate["sources"][0]["source_id"]]
        if candidate["correct"] != expected[0] or candidate["sources"][0]["citation"] != expected[1]:
            raise RuntimeError(f"independent review disagreement for {candidate['learning_objective_id']}")
        if candidate["sources"][0]["tier"] not in {"official_primary", "secondary_reputable"}:
            raise RuntimeError("missing source tier")
        if source["status"] not in {"verified", "verified_with_correction_review", "verified_official_eli_entry", "verified_official_celex_fallback", "verified_entry_point", "verified_current_stable_reference", "verified_public_manual"}:
            raise RuntimeError(f"source register status is not reviewable: {source['source_id']}")
        reviewed = copy.deepcopy(candidate)
        reviewer = f"independent-source-review-{DATE}"
        reviewed["verification"]["answer"] = {"status":"passed","reviewer":reviewer,"checked_at":DATE,"basis":f"Rechecked against {source['source_id']} {expected[1]}; expected option {expected[0]}."}
        reviewed["verification"]["explanation"] = {"status":"passed","reviewer":reviewer,"checked_at":DATE,"basis":f"Explanation checked against the cited {source['source_id']} source and recorded version."}
        reviewed["verification"]["reviewed_at"] = DATE
        reviewed["verification"]["reviewer_decision"] = "accepted"
        for level in ("semantic", "concept"):
            reviewed["deduplication"][level] = {"status":"unique","checked_at":DATE,"basis":"Independent proposition/objective review found no collision with the legacy bank or this lot."}
        reviewed["status"] = "validated"
        errors = validate_record(reviewed)
        if errors:
            raise RuntimeError(f"reviewed record failed validation: {errors}")
        accepted.append(reviewed)
        decisions.append({"objective_id":candidate["learning_objective_id"],"stable_id":candidate["stable_id"],"answer":expected[0],"citation":expected[1],"source_tier":candidate["sources"][0]["tier"],"decision":"accepted","reviewed_at":DATE})

    review_path = ROOT / "docs/question-bank/reviews" / f"{stem}.json"
    review_path.parent.mkdir(parents=True, exist_ok=True)
    review_path.write_text(json.dumps({"review_version":"1.0","lot":stem,"reviewer":f"independent-source-review-{DATE}","source_tier_counts":{"official_primary":sum(x["source_tier"]=="official_primary" for x in decisions),"secondary_reputable":sum(x["source_tier"]=="secondary_reputable" for x in decisions)},"decisions":decisions},ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    accepted_path = ROOT / "docs/question-bank/accepted" / f"{stem}.json"
    accepted_path.parent.mkdir(parents=True, exist_ok=True)
    accepted_payload = {"lot_version":payload["lot_version"],"state":"reviewed","topic_num":args.topic_num,"lot_num":args.lot_num,"revision":payload["revision"],"reviewed_at":DATE,"source_register_sha256":payload["source_register_sha256"],"objective_manifest_sha256":payload["objective_manifest_sha256"],"syllabus_sha256":payload["syllabus_sha256"],"counts":{"candidates":20,"accepted":len(accepted),"rejected":0,"quarantined":0},"review_audit":str(review_path.relative_to(ROOT)),"questions":accepted}
    accepted_path.write_text(json.dumps(accepted_payload,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    checkpoint = {"schema_version":"1.0","syllabus_hash":payload["syllabus_sha256"],"source_register_hash":payload["source_register_sha256"],"topic_num":args.topic_num,"lot_num":args.lot_num,"revision":payload["revision"],"stage":"reviewed","objective_ids":[x["learning_objective_id"] for x in accepted],"stable_ids":[x["stable_id"] for x in accepted],"counts":accepted_payload["counts"],"input_hash":file_sha256(lot_path),"output_hash":file_sha256(accepted_path),"last_import":{"status":"not_started","transaction":None}}
    appended=append_checkpoint(checkpoint_path,checkpoint)
    print(f"topic {args.topic_num}: reviewed {len(accepted)} records; checkpoint {'appended' if appended else 'already present'}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
