if (new java.io.File(new String(${input$path})).isDirectory()) {
	// Récupérer la liste des fichiers et sous-dossiers dans le dossier
	java.io.File[] fichiers = new java.io.File(new String(${input$path})).listFiles();
	// Parcourir la liste et supprimer chaque fichier/dossier
	if (fichiers != null){
		for (java.io.File fichier : fichiers) {
			fichier.delete();
		}
	}
	if (new java.io.File(new String(${input$path})).listFiles() != null){
		new java.io.File(new String(${input$path})).delete();
	}else {
		System.out.println("Unable to delete the folder, it seems that a file was recreated after deleting all the files");
	}
}