if (${input$player} instanceof Player || ${input$player} instanceof ServerPlayer) {
    if (world instanceof ServerLevel _level) 
        _level.getServer().getCommands().performPrefixedCommand(
                new CommandSourceStack(CommandSource.NULL, new Vec3((${input$player}.getX()), (${input$player}.getY()), (${input$player}.getZ())), Vec2.ZERO, _level, 4, "", Component.literal(""), _level.getServer(), null).withSuppressedOutput(),
                ("title " + ${input$player}.getDisplayName().getString() + " subtitle \"" + ${input$subtitle} + "\"")
        );
    if (world instanceof ServerLevel _level)
        _level.getServer().getCommands().performPrefixedCommand(
                new CommandSourceStack(CommandSource.NULL, new Vec3((${input$player}.getX()), (${input$player}.getY()), (${input$player}.getZ())), Vec2.ZERO, _level, 4, "", Component.literal(""), _level.getServer(), null).withSuppressedOutput(),
                ("title " + ${input$player}.getDisplayName().getString() + " times " + ${input$fadein} + ${input$duration} + ${input$fadeout})
        );
    if (world instanceof ServerLevel _level)
        _level.getServer().getCommands().performPrefixedCommand(
                new CommandSourceStack(CommandSource.NULL, new Vec3((${input$player}.getX()), (${input$player}.getY()), (${input$player}.getZ())), Vec2.ZERO, _level, 4, "", Component.literal(""), _level.getServer(), null).withSuppressedOutput(),
                ("title " + ${input$player}.getDisplayName().getString() + " title \"" + ${input$title} + "\"")
        );
}