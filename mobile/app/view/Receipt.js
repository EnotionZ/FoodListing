Ext.define("YourTable.view.Receipt", {
	extend: "Ext.Panel",
	xtype: "receiptPanel",
	id: "foodItemListing",
	config: {
		styleHtmlContent: true,
		items: [
			{
				docked: 'top',
				xtype: 'toolbar',
				items: [
					{
						xtype: 'button',
						ui: 'back',
						text: 'Back'
					},
                    {   xtype: 'spacer'   },
					{
						id: 'showAddCard',
						xtype: 'button',
						iconCls: 'add',
						iconMask: true
					}
				]
			}
		],
		fullscreen: true
	}
});
