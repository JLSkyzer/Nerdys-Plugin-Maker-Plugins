String cheminDossier = ${input$path};

java.io.File dossier = new java.io.File(cheminDossier);

if (dossier.exists() && dossier.isDirectory()) {
    java.io.File[] fichiers = dossier.listFiles();
    
    // Parcours tous les fichiers du dossier
    for (java.io.File currentFile : fichiers) {
        // ...
		${statement$boucle}
    }
} else {
    System.out.println("Le dossier n'existe pas ou n'est pas un dossier valide.");
}