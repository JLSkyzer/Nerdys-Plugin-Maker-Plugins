(new Object() {
	String getID() {
		ResourceLocation itemId = ${input$item}.getItem().getRegistryName();
		String idString = itemId.toString();
		return idString;
	}
}.getID())