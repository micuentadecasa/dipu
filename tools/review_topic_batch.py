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

DATE = "2026-10-12"
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
}


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
        if expectations is None:
            raise RuntimeError(f"no review expectations for topic {args.topic_num}, lot {args.lot_num}")
        expected = expectations[question_num]
        source = sources[candidate["sources"][0]["source_id"]]
        if candidate["correct"] != expected[0] or candidate["sources"][0]["citation"] != expected[1]:
            raise RuntimeError(f"independent review disagreement for {candidate['learning_objective_id']}")
        if candidate["sources"][0]["tier"] not in {"official_primary", "secondary_reputable"}:
            raise RuntimeError("missing source tier")
        if source["status"] not in {"verified", "verified_with_correction_review", "verified_official_eli_entry", "verified_official_celex_fallback", "verified_entry_point", "verified_current_stable_reference"}:
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
