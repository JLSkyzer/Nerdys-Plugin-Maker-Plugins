int radius = ${input$size}; // Rayon du carré en X et Z
int maxY = world.getHeight(); // Couche maximale en Y

net.minecraft.world.entity.Entity skyentity = entity;

int startX = (int) skyentity.getBlockX() - (radius / 2);
int startZ = (int) skyentity.getBlockZ() - (radius / 2);

List<BlockPos> blockPositions = new ArrayList<>();

for (int xPos = startX; xPos < startX + radius; xPos++) {
    for (int zPos = startZ; zPos < startZ + radius; zPos++) {
        for (int yPos = 0; yPos < maxY; yPos++) {
            BlockPos blockPos = new BlockPos(xPos, yPos, zPos);
            blockPositions.add(blockPos);
        }
    }
}

for (BlockPos blockPos : blockPositions) {
    BlockState ${input$blockIterrator} = world.getBlockState(blockPos);

    // Effectuez ici les opérations souhaitées sur le bloc trouvé
	${statement$boucle}
}