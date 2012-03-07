Ext.define("YourTable.view.Session", {
	extend: "Ext.Panel",
	xtype: "sessionPanel",
	config: {
		styleHtmlContent: true,
		items: [
			{
				docked: 'top',
				xtype: 'titlebar',
				title: 'Record your Receipt'
			},
			{
				xtype: 'button',
				text: 'Take a Picture',
				id: 'takePicture',
				ui: 'action',
				iconCls: 'star',
				iconMask: true,
				padding: 10,
				margin: 10
			},
			{
				xtype: 'button',
				text: 'Enter Receipt Info',
				id: 'enterReceipt',
				ui: 'action',
				iconCls: 'add',
				iconMask: true,
				padding: 10,
				margin: 10,
				items: [{ xtype: "receiptPanel" }]
			}
		],
		fullscreen: true
	}
});
