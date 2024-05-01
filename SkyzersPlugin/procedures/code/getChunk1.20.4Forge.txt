new Object(){
	private String getChunk(int chunkX, int chunkZ){
		ChunkPos chunkpos = new ChunkPos(new BlockPos(chunkX, 0, chunkZ));

		return new String(chunkpos.getRegionLocalX() + "-" + chunkpos.getRegionLocalZ());
	}
}.getChunk((int) ${input$locationX}, (int) ${input$locationZ})