INSERT INTO zno_people
         (OUTID , BIRTH , SEXTYPENAME , REGNAME , AREANAME , TERNAME , REGTYPENAME , TerTypeName , ClassProfileNAME ,
         ClassLangName , EONAME , EOTYPENAME , EORegName , EOAreaName , EOTerName , EOParent) SELECT OUTID, BIRTH , SEXTYPENAME , REGNAME , AREANAME , TERNAME , REGTYPENAME , TerTypeName , ClassProfileNAME ,
         ClassLangName , EONAME , EOTYPENAME , EORegName , EOAreaName , EOTerName , EOParent FROM ZNO;

INSERT INTO zno_ukr
             (OUTID, UkrTest , UkrTestStatus , UkrBall100 , UkrBall12 , UkrBall , UkrAdaptScale , UkrPTName , UkrPTRegName , UkrPTAreaName , UkrPTTerName , YEAR )  SELECT OUTID, UkrTest , UkrTestStatus , UkrBall100 , UkrBall12 , UkrBall , UkrAdaptScale , UkrPTName , UkrPTRegName , UkrPTAreaName , UkrPTTerName , YEAR FROM ZNO;

INSERT INTO zno_hist
             (OUTID , histTest , HistLang , histTestStatus , histBall100 , histBall12 , histBall , histPTName , histPTRegName , histPTAreaName , histPTTerName , YEAR  ) SELECT OUTID , histTest , HistLang , histTestStatus , histBall100 , histBall12 , histBall , histPTName , histPTRegName , histPTAreaName , histPTTerName , YEAR FROM ZNO;

INSERT INTO zno_math
             (OUTID, mathTest , mathLang , mathTestStatus , mathBall100 , mathBall12 , mathBall , mathPTName , mathPTRegName , mathPTAreaName , mathPTTerName , YEAR  ) SELECT OUTID, mathTest , mathLang , mathTestStatus , mathBall100 , mathBall12 , mathBall , mathPTName , mathPTRegName , mathPTAreaName , mathPTTerName , YEAR FROM ZNO;

INSERT INTO zno_phys
             (OUTID, physTest , physLang , physTestStatus ,  physBall100 , physBall12 , physBall , physPTName , physPTRegName , physPTAreaName , physPTTerName , YEAR  ) SELECT OUTID, physTest , physLang , physTestStatus ,  physBall100 , physBall12 , physBall , physPTName , physPTRegName , physPTAreaName , physPTTerName , YEAR FROM ZNO;

INSERT INTO zno_chem
             (OUTID, chemTest , chemLang , chemTestStatus , chemBall100 , chemBall12 , chemBall , chemPTName , chemPTRegName , chemPTAreaName , chemPTTerName , YEAR  ) SELECT OUTID, chemTest , chemLang , chemTestStatus , chemBall100 , chemBall12 , chemBall , chemPTName , chemPTRegName , chemPTAreaName , chemPTTerName , YEAR  FROM ZNO;

INSERT INTO zno_bio
             (OUTID, bioTest , bioLang , bioTestStatus , bioBall100 , bioBall12 , bioBall ,bioPTName , bioPTRegName , bioPTAreaName , bioPTTerName , YEAR  ) SELECT OUTID, bioTest , bioLang , bioTestStatus , bioBall100 , bioBall12 , bioBall ,bioPTName , bioPTRegName , bioPTAreaName , bioPTTerName , YEAR FROM ZNO;

INSERT INTO zno_geo
             (OUTID, geoTest , geoLang , geoTestStatus , geoBall100 , geoBall12 , geoBall , geoPTName , geoPTRegName , geoPTAreaName , geoPTTerName , YEAR  ) SELECT OUTID, geoTest , geoLang , geoTestStatus , geoBall100 , geoBall12 , geoBall , geoPTName , geoPTRegName , geoPTAreaName , geoPTTerName , YEAR FROM ZNO;

INSERT INTO zno_eng
             (OUTID, engTest , engTestStatus , engBall100 , engBall12 , engDPALevel , engBall , engPTName , engPTRegName , engPTAreaName , engPTTerName , YEAR  ) SELECT OUTID, engTest , engTestStatus , engBall100 , engBall12 , engDPALevel , engBall , engPTName , engPTRegName , engPTAreaName , engPTTerName , YEAR FROM ZNO;

INSERT INTO zno_fra
             (OUTID, fraTest , fraTestStatus , fraBall100 , fraBall12 , fraDPALevel , fraBall , fraPTName , fraPTRegName , fraPTAreaName , fraPTTerName , YEAR  ) SELECT OUTID, fraTest , fraTestStatus , fraBall100 , fraBall12 , fraDPALevel , fraBall , fraPTName , fraPTRegName , fraPTAreaName , fraPTTerName , YEAR FROM ZNO;

INSERT INTO zno_deu
             (OUTID, deuTest , deuTestStatus , deuBall100 , deuBall12 , deuDPALevel , deuBall , deuPTName , deuPTRegName , deuPTAreaName , deuPTTerName , YEAR  ) SELECT OUTID, deuTest , deuTestStatus , deuBall100 , deuBall12 , deuDPALevel , deuBall , deuPTName , deuPTRegName , deuPTAreaName , deuPTTerName , YEAR FROM ZNO;

INSERT INTO zno_spa
             (OUTID, spaTest , spaTestStatus , spaBall100 , spaBall12 , spaDPALevel , spaBall , spaPTName , spaPTRegName , spaPTAreaName , spaPTTerName , YEAR  ) SELECT OUTID, spaTest , spaTestStatus , spaBall100 , spaBall12 , spaDPALevel , spaBall , spaPTName , spaPTRegName , spaPTAreaName , spaPTTerName , YEAR  FROM ZNO;

