# Ruleaza: python3 descarca_imagini.py  (descarca 30 imagini de pe Wikimedia Commons in folderul curent)
import json,urllib.request,urllib.parse,sys,os,time
Q=[("01_tablita_ceara_romana","Roman wax tablet stylus"),
("02_Decebalus_per_Scorilo","Decebalus per Scorilo"),
("03_dictionar_vechi","Lexicon Budense"),
("04_Lupa_Capitolina","Capitoline Wolf Musei Capitolini"),
("05_Forul_Roman","Roman Forum panorama"),
("06_bust_Traian","Bust of Trajan Glyptothek"),
("07_Columna_lui_Traian","Trajan's Column Rome"),
("08_Columna_moartea_lui_Decebal","Trajan's Column Decebalus suicide"),
("09_Columna_trecerea_Dunarii","Trajan's Column crossing Danube pontoon bridge"),
("10_Tropaeum_Traiani","Tropaeum Traiani Adamclisi"),
("11_Podul_lui_Apolodor_Drobeta","Trajan's Bridge Drobeta ruins"),
("12_Chipul_lui_Decebal_Cazane","Rock sculpture of Decebalus"),
("13_Sarmizegetusa_sanctuar","Sarmizegetusa Regia sanctuary"),
("14_Coiful_de_la_Cotofenesti","Helmet of Cotofenesti"),
("15_Bratari_dacice_aur","Dacian gold bracelets"),
("16_Draco_dacic","Dacian Draco"),
("17_Tezaurul_de_la_Pietroasa","Pietroasele treasure"),
("18_Statuia_Burebista","Burebista statue"),
("19_Statuie_dac_captiv","Statue of a Dacian"),
("20_Muntii_Orastiei","Muntii Orastiei"),
("21_port_popular_Ardeal","Romanian peasants traditional costume Transylvania"),
("22_dac_pe_Columna_detaliu","Trajan's Column Dacian warriors"),
("23_stup_traditional","traditional beehive Romania"),
("24_arat_cu_boii","Romania plowing oxen"),
("25_Nicolae_Densusianu","Nicolae Densusianu"),
("26_Dacia_preistorica","Dacia preistorica Densusianu"),
("27_bust_Herodot","Herodotus bust"),
("28_harta_Dacia_Burebista","Dacia Burebista map"),
("29_final_Sfinxul_Bucegi","Sfinxul Bucegi"),
("30_final_rasarit_Carpati","sunrise Carpathian Mountains Romania")]
H={"User-Agent":"ColajDaci/1.0 (punguleanul personal project)"}
def get(u): return urllib.request.urlopen(urllib.request.Request(u,headers=H),timeout=60).read()
src=[]
for name,q in Q:
  try:
    p=dict(action="query",format="json",generator="search",gsrsearch=q+" filetype:bitmap",gsrnamespace=6,gsrlimit=5,prop="imageinfo",iiprop="url|extmetadata",iiurlwidth=1920)
    d=json.loads(get("https://commons.wikimedia.org/w/api.php?"+urllib.parse.urlencode(p)))
    pages=sorted(d.get("query",{}).get("pages",{}).values(),key=lambda x:x["index"])
    if not pages: print("NONE",name);continue
    ii=pages[0]["imageinfo"][0]; u=ii.get("thumburl") or ii["url"]
    ext=os.path.splitext(u)[1].lower() or ".jpg"
    open(name+ext,"wb").write(get(u))
    lic=ii.get("extmetadata",{}).get("LicenseShortName",{}).get("value","?")
    src.append(f"{name}{ext}\t{pages[0]['title']}\t{lic}\t{ii['descriptionurl']}")
    print("OK",name,pages[0]["title"]); time.sleep(1)
  except Exception as e: print("ERR",name,e)
open("SURSE_si_licente.txt","w").write("\n".join(src)+"\n")
