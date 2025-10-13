if (${input$item} != null){
	net.minecraft.nbt.ListTag listTag = new net.minecraft.nbt.ListTag();
	String string = ${input$enchantList};
	//System.out.println("Enchant string : " + string);
	java.util.regex.Pattern pattern = java.util.regex.Pattern.compile("\\{id:\"(.*?)\",lvl:(\\d+)s\\}");
	java.util.regex.Matcher matcher = pattern.matcher(string);
	while (matcher.find()) {
		String id = matcher.group(1);
		int lvl = Integer.parseInt(matcher.group(2));

		net.minecraft.nbt.CompoundTag compoundTag = new net.minecraft.nbt.CompoundTag();
		compoundTag.putString("id", id);
		compoundTag.putInt("lvl", lvl);

		listTag.add(compoundTag);
	}
	net.minecraft.world.item.enchantment.EnchantmentHelper.setEnchantments(net.minecraft.world.item.enchantment.EnchantmentHelper.deserializeEnchantments(listTag), ${input$item});
}