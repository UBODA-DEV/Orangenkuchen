"""
Author: Angelo Oliveira

Ziel: Einen Orangenkuchen backen

1- Schlagen Sie die Eier, den Zucker, das Öl, den Saft und die Orangenschalen im Mixer.
2- Geben Sie die Mischung in eine Schüssel und fügen Sie das Mehl und das Backpulver hinzu.
3- Bereiten Sie die Form vor, fetten und bemehlen Sie sie, falls noch nicht geschehen.
4- Übertragen Sie die Mischung aus der Schüssel in die Form.
5- Backen Sie den Kuchen in der gefetteten und bemehlten Form etwa 30 Minuten lang.
6- Nehmen Sie den Kuchen aus der Form und befeuchten Sie ihn mit Orangensaft.

Pseudocode

alles_mixen(eier, zucker, öl, saft, schalen)
in_schüssel_geben(mischung)
    hinzufügen(mischung, mehl, backpulver)
backform_vorbereiten(form)
    wenn nicht_gefettet_und_bemehlt(form):
        fetten_und_bemehlen(form)
in_form_geben(mischung, form)
kuchen_backen(form, 30_minuten)
kuchen_ausformen(form)
kuchen_traenken(kuchen, orangensaft)

"""
# Code für die Zubereitung eines Orangenkuchens mit Benutzerinteraktion

def auf_bestaetigung_warten(nachricht="Drücken Sie Enter, um fortzufahren..."):
    input(nachricht)

def alles_mixen(eier, zucker, oel, saft, schalen):
    print("Bereite vor, die Zutaten im Mixer zu mischen...")
    print(f"Verfügbare Zutaten: {eier}, {zucker}, {oel}, {saft} und {schalen}")
    auf_bestaetigung_warten("Drücken Sie Enter, um alles im Mixer zu mischen...")
    
    print("Mixe Eier, Zucker, Öl, Saft und Schalen im Mixer...")
    auf_bestaetigung_warten("Gemischt! Drücken Sie Enter, um fortzufahren...")
    return "fertige_mischung"

def in_schuessel_geben(mischung):
    print(f"Die {mischung} ist im Mixer fertig.")
    auf_bestaetigung_warten("Drücken Sie Enter, um die Mischung in eine Schüssel zu geben...")
    
    print("Gebe die Mischung in eine Schüssel...")
    auf_bestaetigung_warten("Übertragung abgeschlossen! Drücken Sie Enter, um fortzufahren...")
    return mischung

def hinzufuegen(mischung, mehl, backpulver):
    print(f"Die {mischung} ist in der Schüssel. Bereite vor, trockene Zutaten hinzuzufügen.")
    print(f"Zutaten zum Hinzufügen: {mehl} und {backpulver}")
    auf_bestaetigung_warten("Drücken Sie Enter, um Mehl und Backpulver hinzuzufügen...")
    
    print("Füge Mehl und Backpulver zur Mischung hinzu...")
    auf_bestaetigung_warten("Zutaten hinzugefügt! Drücken Sie Enter, um fortzufahren...")
    return "fertiger_teig"

def backform_vorbereiten(form):
    print("Überprüfe die Backform...")
    
    if not form["eingefettet_und_bemehlt"]:
        print("Die Form muss eingefettet und bemehlt werden.")
        auf_bestaetigung_warten("Drücken Sie Enter, um die Form einzufetten und zu bemehlen...")
        
        print("Fette die Form ein und bemehle sie...")
        form["eingefettet_und_bemehlt"] = True
        auf_bestaetigung_warten("Form vorbereitet! Drücken Sie Enter, um fortzufahren...")
    else:
        print("Die Form ist bereits eingefettet und bemehlt.")
        auf_bestaetigung_warten("Drücken Sie Enter, um fortzufahren...")
    
    return form

def in_form_geben(mischung, form):
    print(f"Der {mischung} ist in der Schüssel fertig.")
    print("Die Form ist eingefettet und bemehlt.")
    auf_bestaetigung_warten("Drücken Sie Enter, um den Teig in die Form zu geben...")
    
    print("Gebe den Teig in die Form...")
    form["inhalt"] = mischung
    auf_bestaetigung_warten("Teig übertragen! Drücken Sie Enter, um fortzufahren...")

def kuchen_backen(form, zeit):
    print(f"Die Form mit dem Teig ist bereit zum Backen.")
    auf_bestaetigung_warten(f"Drücken Sie Enter, um den Kuchen für {zeit} Minuten zu backen...")
    
    print(f"Backe den Kuchen in der Form für {zeit} Minuten...")
    print("Warten Sie, während der Kuchen backt...")
    auf_bestaetigung_warten("Zeit abgelaufen! Kuchen gebacken. Drücken Sie Enter, um fortzufahren...")
    return "gebackener_kuchen"

def kuchen_ausformen(form):
    print("Der Kuchen ist gebacken und bereit zum Ausformen.")
    auf_bestaetigung_warten("Drücken Sie Enter, um den Kuchen auszuformen...")
    
    print("Forme den Kuchen aus...")
    auf_bestaetigung_warten("Kuchen ausgeformt! Drücken Sie Enter, um fortzufahren...")
    return "ausgeformter_kuchen"

def kuchen_traenken(kuchen, orangensaft):
    print(f"Der {kuchen} ist ausgeformt und bereit für den Saft.")
    auf_bestaetigung_warten(f"Drücken Sie Enter, um den Kuchen mit {orangensaft} zu tränken...")
    
    print("Tränke den Kuchen mit Orangensaft...")
    auf_bestaetigung_warten("Kuchen getränkt! Drücken Sie Enter, um abzuschließen...")
    return "fertiger_kuchen"

# Einstiegspunkt des Programms
if __name__ == "__main__":
    print("=== INTERAKTIVES PROGRAMM ZUR ZUBEREITUNG EINES ORANGENKUCHENS ===")
    print("Dieses Programm führt Sie durch die Zubereitung eines Orangenkuchens.")
    print("Bei jedem Schritt werden Sie aufgefordert, zu bestätigen, um fortzufahren.")
    auf_bestaetigung_warten("Drücken Sie Enter, um zu beginnen...")
    
    # Definition der Zutaten als einfache Strings
    eier = "Eier"
    zucker = "Zucker"
    oel = "Öl"
    saft = "Orangensaft"
    schalen = "Orangenschalen"
    mehl = "Mehl"
    backpulver = "Backpulver"
    
    # Anzeigen der benötigten Zutaten
    print("\n=== BENÖTIGTE ZUTATEN ===")
    print(f"- {eier}")
    print(f"- {zucker}")
    print(f"- {oel}")
    print(f"- {saft}")
    print(f"- {schalen}")
    print(f"- {mehl}")
    print(f"- {backpulver}")
    auf_bestaetigung_warten("\nDrücken Sie Enter, wenn Sie alle Zutaten haben...")
    
    # Erstellung des Wörterbuchs, das die Form repräsentiert
    form = {"eingefettet_und_bemehlt": False, "inhalt": None}

    # Ausführung der Schrittsequenz zur Herstellung des Kuchens
    print("\n=== BEGINNE MIT DER ZUBEREITUNG DES KUCHENS ===")
    mischung = alles_mixen(eier, zucker, oel, saft, schalen)
    mischung = in_schuessel_geben(mischung)
    teig = hinzufuegen(mischung, mehl, backpulver)
    form = backform_vorbereiten(form)
    in_form_geben(teig, form)
    kuchen = kuchen_backen(form, 30)
    kuchen = kuchen_ausformen(form)
    kuchen = kuchen_traenken(kuchen, saft)

    # Abschlussnachricht, die anzeigt, dass der Kuchen fertig ist
    print("\n=== HERZLICHEN GLÜCKWUNSCH! ===")
    print("Orangenkuchen ist servierfertig!")
    print("Genießen Sie Ihr leckeres Rezept.")