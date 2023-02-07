"""lokaman"""
from pyrogram.types import (InlineKeyboardButton, InlineKeyboardMarkup,ForceReply)
from pyrogram import Client , filters

@Client.on_callback_query(filters.regex('upgrade'))
async def upgrade(bot,update):
	text = """**Free Plan User**
	Daily  Upload limit 1.2GB
	Price 0
	
	**🪙 Silver Tier 🪙** 
	Daily  Upload  limit 10GB
	Price Rs 20  ind /🌎  per Month
	
	**💫 Gold Tier 💫**
	Daily Upload limit 50GB
	Price Rs 50  ind /🌎  per Month
	
	**💎 Diamond 💎**
	Daily Upload limit 100GB
	Price Rs 100  ind /🌎  per Month
	
	
	Pay Using Upi I'd ```8194994597@paytm```
	
	After Payment Send Screenshots Of 
        Payment To Admin @sheffy_samra"""
	keybord = InlineKeyboardMarkup([[ 
        			InlineKeyboardButton("ADMIN 🛂",url = "https://t.me/sheffy_samra")], 
        			[InlineKeyboardButton("Paytm",url = "https://p.paytm.me/xCTH/vo37hii9"),
        			InlineKeyboardButton("Paytm",url = "https://p.paytm.me/xCTH/vo37hii9")],[InlineKeyboardButton("Cancel",callback_data = "cancel")  ]])
	await update.message.edit(text = text,reply_markup = keybord)
	

@Client.on_message(filters.private & filters.command(["upgrade"]))
async def upgradecm(bot,message):
	text = """**Free Plan User**
	Daily  Upload limit 1.2GB
	Price 0
	
	**🪙 Silver Tier 🪙** 
	Daily  Upload  limit 10GB
	Price Rs 20  ind /🌎  per Month
	
	**💫 Gold Tier 💫**
	Daily Upload limit 50GB
	Price Rs 50  ind /🌎  per Month
	
	**💎 Diamond 💎**
	Daily Upload limit 100GB
	Price Rs 100  ind /🌎  per Month
	
	
	Pay Using Upi I'd ```8194994597@paytm```
	
	After Payment Send Screenshots Of 
        Payment To Admin @sheffy_samra"""
	keybord = InlineKeyboardMarkup([[ 
        			InlineKeyboardButton("ADMIN 🛂",url = "https://t.me/sheffy_samra")], 
        			[InlineKeyboardButton("Paytm",url = "https://p.paytm.me/xCTH/vo37hii9"),
        			InlineKeyboardButton("Paytm",url = "https://p.paytm.me/xCTH/vo37hii9")],[InlineKeyboardButton("Cancel",callback_data = "cancel")  ]])
	await message.reply_text(text = text,reply_markup = keybord)
