if (new java.io.File(new String(${input$path})).exists()) { // Vérifie si le fichier existe avant de le supprimer
	// Supprime le fichier
	boolean suppressionReussie = new java.io.File(${input$path}).delete();

	if (suppressionReussie) {
		System.out.println("Le fichier a été supprimé avec succès.");
	} else {
		System.out.println("Impossible de supprimer le fichier.");
	}
} else {
	System.out.println("Le fichier n'existe pas.");
}