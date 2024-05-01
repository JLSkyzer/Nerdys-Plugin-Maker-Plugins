{
	if (world.isClientSide()){
		if (${input$entity} instanceof LivingEntity livingEntity) {
			livingEntity.hurtDuration = 10;
			livingEntity.hurtTime = livingEntity.hurtDuration;
		}
	}
	
}