Ext.define("YourTable.view.Main", {
	extend: 'Ext.tab.Panel',
	requires: ['Ext.TitleBar'],

	config: {
		tabBarPosition: 'bottom',

		items: [
			{
				title: 'Add Receipt',
				iconCls: 'compose',

				styleHtmlContent: true,
				scrollable: true,
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
						margin: 10
					}
				]
			},
			{
				title: 'History',
				iconCls: 'maps',
				items: [
					{
						docked: 'top',
						xtype: 'titlebar',
						title: 'See dining history'
					}
				]
			},
			{
				title: 'Account',
				iconCls: 'user',
				items: [
					{
						docked: 'top',
						xtype: 'titlebar',
						title: 'Manage Account'
					}
				]
			},
			{
				title: 'Settings',
				iconCls: 'settings',
				items: [
					{
						docked: 'top',
						xtype: 'titlebar',
						title: 'Change Settings'
					}
				]
			}
		]
	}
});