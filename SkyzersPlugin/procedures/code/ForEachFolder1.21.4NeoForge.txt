String cheminDossierParent = ${input$path};

java.io.File dossierParent = new java.io.File(cheminDossierParent);

if (dossierParent.exists() && dossierParent.isDirectory()) {
    java.io.File[] sousDossiers = dossierParent.listFiles();

    // Parcours tous les sous-dossiers du dossier parent
    for (java.io.File currentFolder : sousDossiers) {
        if (currentFolder.isDirectory()) {
            // ...
            ${statement$boucle}
        }
    }
} else {
    System.out.println("Le dossier parent n'existe pas ou n'est pas un dossier valide.");
}