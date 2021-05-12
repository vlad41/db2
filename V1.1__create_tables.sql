CREATE TABLE IF NOT EXISTS zno_people
     (Id SERIAL PRIMARY KEY, OUTID TEXT UNIQUE, BIRTH INTEGER, SEXTYPENAME TEXT, REGNAME TEXT, AREANAME TEXT, TERNAME TEXT, REGTYPENAME TEXT, TerTypeName TEXT, ClassProfileNAME TEXT,
     ClassLangName TEXT, EONAME TEXT, EOTYPENAME TEXT, EORegName TEXT, EOAreaName TEXT, EOTerName TEXT, EOParent TEXT);

CREATE TABLE IF NOT EXISTS zno_ukr
     (Id SERIAL PRIMARY KEY, OUTID TEXT UNIQUE, UkrTest TEXT, UkrTestStatus TEXT, UkrBall100 REAL,
     UkrBall12 REAL, UkrBall REAL, UkrAdaptScale TEXT, UkrPTName TEXT, UkrPTRegName TEXT, UkrPTAreaName TEXT, UkrPTTerName TEXT, YEAR INTEGER );

CREATE TABLE IF NOT EXISTS zno_hist
     (Id SERIAL PRIMARY KEY, OUTID TEXT UNIQUE, histTest TEXT, HistLang TEXT, histTestStatus TEXT,
        histBall100 REAL, histBall12 REAL, histBall REAL, histPTName TEXT, histPTRegName TEXT, histPTAreaName TEXT, histPTTerName TEXT, YEAR INTEGER );

CREATE TABLE IF NOT EXISTS zno_math
     (Id SERIAL PRIMARY KEY, OUTID TEXT UNIQUE, mathTest TEXT, mathLang TEXT, mathTestStatus TEXT,
        mathBall100 REAL, mathBall12 REAL, mathBall REAL, mathPTName TEXT, mathPTRegName TEXT, mathPTAreaName TEXT, mathPTTerName TEXT, YEAR INTEGER );

CREATE TABLE IF NOT EXISTS zno_phys
     (Id SERIAL PRIMARY KEY, OUTID TEXT UNIQUE, physTest TEXT, physLang TEXT, physTestStatus TEXT,
         physBall100 REAL, physBall12 REAL, physBall REAL, physPTName TEXT, physPTRegName TEXT, physPTAreaName TEXT, physPTTerName TEXT, YEAR INTEGER );

CREATE TABLE IF NOT EXISTS zno_chem
     (Id SERIAL PRIMARY KEY, OUTID TEXT UNIQUE, chemTest TEXT, chemLang TEXT, chemTestStatus TEXT, chemBall100 REAL,
          chemBall12 REAL, chemBall REAL, chemPTName TEXT, chemPTRegName TEXT, chemPTAreaName TEXT, chemPTTerName TEXT, YEAR INTEGER );

CREATE TABLE IF NOT EXISTS zno_bio
     (Id SERIAL PRIMARY KEY, OUTID TEXT UNIQUE, bioTest TEXT, bioLang TEXT, bioTestStatus TEXT, bioBall100 REAL, bioBall12 REAL,
     bioBall REAL,bioPTName TEXT, bioPTRegName TEXT, bioPTAreaName TEXT, bioPTTerName TEXT, YEAR INTEGER );

CREATE TABLE IF NOT EXISTS zno_geo
     (Id SERIAL PRIMARY KEY, OUTID TEXT UNIQUE, geoTest TEXT, geoLang TEXT, geoTestStatus TEXT, geoBall100 REAL, geoBall12 REAL,
     geoBall REAL, geoPTName TEXT, geoPTRegName TEXT, geoPTAreaName TEXT, geoPTTerName TEXT, YEAR INTEGER );

CREATE TABLE IF NOT EXISTS zno_eng
     (Id SERIAL PRIMARY KEY, OUTID TEXT UNIQUE, engTest TEXT, engTestStatus TEXT, engBall100 REAL, engBall12 REAL, engDPALevel TEXT,
     engBall REAL, engPTName TEXT, engPTRegName TEXT, engPTAreaName TEXT, engPTTerName TEXT, YEAR INTEGER );

CREATE TABLE IF NOT EXISTS zno_fra
     (Id SERIAL PRIMARY KEY, OUTID TEXT UNIQUE, fraTest TEXT, fraTestStatus TEXT, fraBall100 REAL, fraBall12 REAL, fraDPALevel TEXT,
     fraBall REAL, fraPTName TEXT, fraPTRegName TEXT, fraPTAreaName TEXT, fraPTTerName TEXT, YEAR INTEGER );

CREATE TABLE IF NOT EXISTS zno_deu
     (Id SERIAL PRIMARY KEY, OUTID TEXT UNIQUE, deuTest TEXT, deuTestStatus TEXT, deuBall100 REAL, deuBall12 REAL, deuDPALevel TEXT,
     deuBall REAL, deuPTName TEXT, deuPTRegName TEXT, deuPTAreaName TEXT, deuPTTerName TEXT, YEAR INTEGER );

CREATE TABLE IF NOT EXISTS zno_spa
     (Id SERIAL PRIMARY KEY, OUTID TEXT UNIQUE, spaTest TEXT, spaTestStatus TEXT, spaBall100 REAL, spaBall12 REAL, spaDPALevel TEXT,
     spaBall REAL, spaPTName TEXT, spaPTRegName TEXT, spaPTAreaName TEXT, spaPTTerName TEXT, YEAR INTEGER );
