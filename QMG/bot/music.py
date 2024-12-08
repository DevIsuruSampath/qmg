from pyrogram import Client, filters
from pyrogram.types import Message
from QMG.plugins.ytsearch import search_and_download
import os
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@Client.on_message(filters.command("music") & filters.private)
async def music_handler(client, message: Message):
    query = " ".join(message.command[1:])
    if not query:
        await message.reply_text("Please provide a song name or YouTube link.")
        return

    status_message = await message.reply_text(f"🔍 Searching for `{query}`...")

    try:
        # Call the search and download function
        file_path = await search_and_download(query)

        # Send the downloaded audio file back to the user
        await client.send_audio(
            chat_id=message.chat.id,
            audio=file_path,
            caption=f"🎶 Here is your song: `{query}`",
            performer="YouTube",
            title=os.path.basename(file_path).rsplit('.', 1)[0]
        )

        # Log the success
        logger.info(f"Successfully sent the song: {file_path}")

        # Clean up the downloaded file
        os.remove(file_path)
        await status_message.delete()

    except Exception as e:
        # Handle errors and inform the user
        logger.error(f"Error occurred: {e}")
        await status_message.edit_text(f"❌ An error occurred while processing your request:

`{str(e)}`")
