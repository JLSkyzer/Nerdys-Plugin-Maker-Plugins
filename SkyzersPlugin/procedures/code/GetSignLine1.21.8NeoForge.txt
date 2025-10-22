(new Object(){
	public String getSignLineText(Level signWorld, BlockPos pos, int lineNumber) {
		net.minecraft.world.level.block.entity.SignBlockEntity sign = (net.minecraft.world.level.block.entity.SignBlockEntity) signWorld.getBlockEntity(pos);
		if (sign != null) {
			String lineTextComponent = String.valueOf(sign.getFrontText().getMessage(lineNumber, true));
			String lineText = lineTextComponent;
			return lineText;
		}
		return ""; // Retourner une chaîne vide si le bloc n'est pas un panneau en bois ou si le panneau est vide
	}
}.getSignLineText(world, new BlockPos(${input$posX}, ${input$posY}, ${input$posZ}), ${input$line}))