(int) new Object(){
	private double getDamageAfterArmorAbsorb(DamageSource eridamageSource, double eridamage){
		if (!eridamageSource.is(net.minecraft.tags.DamageTypeTags.BYPASSES_ARMOR)) {
			eridamage = net.minecraft.world.damagesource.CombatRules.getDamageAfterAbsorb((float) eridamage, (float)net.minecraft.util.Mth.floor(net.minecraft.world.entity.ai.attributes.Attributes.ARMOR.getDefaultValue()), (float)net.minecraft.world.entity.ai.attributes.Attributes.ARMOR_TOUGHNESS.getDefaultValue());
		}

		return eridamage;
	}
}.getDamageAfterArmorAbsorb(damagesource, (float) ${input$damage})