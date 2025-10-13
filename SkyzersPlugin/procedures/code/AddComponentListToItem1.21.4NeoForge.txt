if (componentList.size() > 0) {
	net.minecraft.nbt.CompoundTag display = ${input$item}.getOrCreateTagElement("display");
	net.minecraft.nbt.ListTag loreItems = new net.minecraft.nbt.ListTag();
	for (net.minecraft.network.chat.Component l : componentList) {
		if (l instanceof net.minecraft.network.chat.MutableComponent) {
			((net.minecraft.network.chat.MutableComponent) l).withStyle(style -> style.withItalic(style.isItalic()));
		}
		loreItems.add(StringTag.valueOf(net.minecraft.network.chat.Component.Serializer.toJson(l)));
	}
	display.put("Lore", loreItems);
}