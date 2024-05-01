new Object(){
	private String getRegion(int chunkX, int chunkZ){
		ChunkPos chunkpos = new ChunkPos(new BlockPos(chunkX, 0, chunkZ));

		return new String("r." + chunkpos.getRegionX() + "." + chunkpos.getRegionZ());
	}
}.getRegion((int) ${input$positionX}, (int) ${input$positionZ})