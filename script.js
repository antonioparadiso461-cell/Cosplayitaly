document.addEventListener("DOMContentLoaded", () => {
    const postsContainer = document.getElementById("blog-posts");
    
    const firstPost = `
        <article>
            <h2>L'Arte del Cosplay: Passione, Dedizione e la Magia della Trasformazione</h2>
            <p><strong>Data:</strong> 10 Agosto 2026</p>
            <p>Il cosplay non è semplicemente l'atto di indossare un costume; è una forma d'arte complessa, un ponte tangibile tra i mondi fantastici che amiamo e la nostra realtà quotidiana. Per chi vive questa passione in prima persona, ogni progetto rappresenta mesi di pianificazione, ricerca dei materiali, studio dei dettagli e ore passate a rifinire ogni singolo elemento sartoriale o di armatura. È un viaggio di dedizione totale che trasforma il fan in co-creatore dell'opera originale.</p>
            
            <p>Nel panorama odierno, la comunità cosplay italiana e globale sta vivendo una rinascita straordinaria. Le fiere di settore non sono più semplici raduni, ma veri e propri palcoscenici internazionali dove la maestria artigianale incontra l'interpretazione scenica. Dalla lavorazione del thermoplastic (Worbla ed EVA foam) fino alla cura meticolosa del make-up e dell'acconciatura delle parrucche, ogni cosplayer investe una parte della propria anima in ciò che realizza. Questo impegno costante eleva il cosplay a dignità di arte contemporanea.</p>
            
            <div class="cosplay-gallery">
                <img src="images/cosplay1.png" alt="Cosplay Principessa Guerriera con Armatura Ornata">
                <img src="images/cosplay2.png" alt="Cosplay Ladro Fantasy con Mantello in Pelle">
                <img src="images/cosplay3.png" alt="Cosplay Maga con Effetti di Magia Dorata">
            </div>

            <p>Analizzando le tendenze recenti, notiamo come l'ispirazione attinga sempre più a piene mani da universi visivi complessi: dai videogiochi next-gen alle serie animate più acclamate, passando per le opere letterarie fantasy e sci-fi. La sfida non risiede unicamente nella fedeltà estetica del costume, ma nella capacità di catturare l'essenza e la personalità del personaggio. Quando un cosplayer indossa i panni del proprio eroe o cattivo preferito, si cala in una performance che richiede presenza scenica, empatia e profonda conoscenza del background narrativo.</p>

            <p>In questo nostro nuovo spazio online, vogliamo celebrare ogni sfaccettatura di questo meraviglioso mondo. Che siate veterani con decine di convention alle spalle o neofiti affascinati da questo universo, troverete approfondimenti, gallerie fotografiche esclusive, recensioni di tecniche e riflessioni sulla cultura pop. Restate sintonizzati: ogni ventiquattro ore pubblicheremo nuovi contenuti, analisi e splendide gallerie fotografiche per alimentare insieme la nostra irrefrenabile passione.</p>
        </article>
    `;

    postsContainer.innerHTML = firstPost;
});
