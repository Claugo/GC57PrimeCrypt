I miei programmi "GC57" sono esclusivamente dimostrativi poiché il mio obiettivo non è evidenziare il sistema di criptazione, ma il metodo di fattorizzazione unico nel suo genere. La proprietà utilizzata da GC57 per fattorizzare i grandi semiprimi si basa sull'aver individuato una chiave generica che abbinata a una certa quantità di semiprimi, diversi tra loro, ma con lo stesso peso in bit, consente di fattorizzarli in tempo O(1), ovvero in meno di un secondo.

Questo processo di fattorizzazione, applicabile a numeri semiprimi già creati e archiviati in file, mantiene la stessa velocità indipendentemente dalla loro dimensione. Ad esempio: 8000 bit, 10000 bit, 13000 bit, ecc.

Sono convinto che questo sistema aprirà nuove prospettive nel concetto di sicurezza e nello studio della teoria dei numeri.

Il progetto, o meglio i progetti GC57crypto, sono nati con l'obiettivo di dare una forma pratica alla mia scoperta. GC57PrimeCrypt è l'ultimo di questi progetti, ma non è l'unico.
Tra tutti, questo progetto si distingue come uno dei più riusciti, poiché combina la complessità della fattorizzazione di grandi semiprimi con l'implementazione di algoritmi avanzati
come SHA-3, PBKDF2 e AES.  Il programma è interamente scritto in Python e include una spiegazione dettagliata dei passaggi necessari per la criptazione sia del testo che dei suoi
eventuali allegati. L'unico elemento mancante nel programma, così come negli altri progetti basati sullo stesso principio, è rappresentato dalle librerie contenenti i semiprimi
pre-generati e le rispettive chiavi. A tal proposito, esiste un altro programma, anch'esso scritto in Python, e che si occupa della creazione di queste librerie. 
Questo programma lo fornirò a chi desidera testare il mio metodo di criptazione. In tal caso è possibile fare richiesta per ottenere gratuitamente il software con annesse
tutte le indicazione per la generazione di quelle librerie .
