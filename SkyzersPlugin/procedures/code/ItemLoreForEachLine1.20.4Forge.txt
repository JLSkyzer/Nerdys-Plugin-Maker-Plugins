if (${input$item} != null && ${input$item}.getOrCreateTagElement("display").get("Lore") != null){
	String result = ${input$item}.getOrCreateTagElement("display").get("Lore").toString();
	result = result.replaceAll("'", "");

	com.google.gson.JsonArray jsonArray = com.google.gson.JsonParser.parseString(result).getAsJsonArray();
	for (int i = 0; i < jsonArray.size(); i++) {
		com.google.gson.JsonObject jsonObject = jsonArray.get(i).getAsJsonObject();
		String text = jsonObject.get("text").getAsString();

		${statement$codeInput}
	}
}