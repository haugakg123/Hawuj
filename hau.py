import discord
from discord.ext import commands
import threading
import time
import re
import requests
import os
import random
import asyncio
import datetime
import json
import base64 
import aiohttp
import traceback
import shutil
import hashlib
from typing import Dict, Any
from threading import Thread
os.system("clear")

# Developer Zerfer w Gabi / 1-5-2025 
print("        B O T - M A D E - B Y - H A W U J💢")
TOKEN = input("\033[31m [GABI BOT]\033[32m Vui lòng nhập token bot:\033[37m ") # Nhập token bot discord
ADMIN_ID = int(input("\033[31m [GABI BOT]\033[32m Vui lòng nhập id admin bot:\033[37m ")) # Nhập id admin bot
admins = []
IDADMIN_GOC = ADMIN_ID

intents = discord.Intents.default()
intents.messages = True
intents.message_content = True
bot = commands.Bot(command_prefix='.', intents=intents)

@bot.event
async def on_ready():
    print(f'\033[35m》{bot.user}《 đã bật chế độ hotwar 2025!')
   
#messenger task 
allowed_users = set()
treo_threads = {}
treo_start_times = {}
messenger_instances = {}
nhay_threads = {}
nhay_start_times = {}
chui_threads = {}
chui_start_times = {}
codelag_threads = {}
codelag_start_times = {}
so_threads = {}
so_start_times = {}
#discord task
start_time = datetime.datetime.utcnow()
UA_KIWI = [
    "Mozilla/5.0 (Linux; Android 11; RMX2185) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6167.140 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; Redmi Note 11) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6099.129 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; Pixel 6a) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.6261.68 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; V2031) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.5938.60 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; CPH2481) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.6312.86 Mobile Safari/537.36"
]

UA_VIA = [
    "Mozilla/5.0 (Linux; Android 10; Redmi Note 8) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/108.0.0.0 Mobile Safari/537.36 Via/4.8.2",
    "Mozilla/5.0 (Linux; Android 11; V2109) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/112.0.5615.138 Mobile Safari/537.36 Via/4.9.0",
    "Mozilla/5.0 (Linux; Android 13; TECNO POVA 5) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.134 Mobile Safari/537.36 Via/5.0.1",
    "Mozilla/5.0 (Linux; Android 12; Infinix X6710) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/115.0.5790.138 Mobile Safari/537.36 Via/5.2.0",
    "Mozilla/5.0 (Linux; Android 14; SM-A546E) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/122.0.6261.112 Mobile Safari/537.36 Via/5.3.1"
]

USER_AGENTS = UA_KIWI + UA_VIA

class Messenger:
    def __init__(self, cookie):
        self.cookie = cookie
        self.user_id = self.id_user()
        self.user_agent = random.choice(USER_AGENTS)
        self.fb_dtsg = None
        self.init_params()

    def id_user(self):
        try:
            c_user = re.search(r"c_user=(\d+)", self.cookie).group(1)
            return c_user
        except:
            raise Exception("Cookie không hợp lệ")

    def init_params(self):
        headers = {
            'Cookie': self.cookie,
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.9,vi;q=0.8',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'none',
            'Sec-Fetch-User': '?1',
            'Upgrade-Insecure-Requests': '1'
        }

        try:
            response = requests.get('https://www.facebook.com', headers=headers)
            fb_dtsg_match = re.search(r'"token":"(.*?)"', response.text)

            if not fb_dtsg_match:
                response = requests.get('https://mbasic.facebook.com', headers=headers)
                fb_dtsg_match = re.search(r'name="fb_dtsg" value="(.*?)"', response.text)

                if not fb_dtsg_match:
                    response = requests.get('https://m.facebook.com', headers=headers)
                    fb_dtsg_match = re.search(r'name="fb_dtsg" value="(.*?)"', response.text)

            if fb_dtsg_match:
                self.fb_dtsg = fb_dtsg_match.group(1)
            else:
                raise Exception("Không thể lấy được fb_dtsg")

        except Exception as e:
            raise Exception(f"Lỗi khi khởi tạo tham số: {str(e)}")

    def gui_tn(self, recipient_id, message, max_retries=10):
        for attempt in range(max_retries):
            timestamp = int(time.time() * 1000)
            offline_threading_id = str(timestamp)
            message_id = str(timestamp)

            data = {
                'thread_fbid': recipient_id,
                'action_type': 'ma-type:user-generated-message',
                'body': message,
                'client': 'mercury',
                'author': f'fbid:{self.user_id}',
                'timestamp': timestamp,
                'source': 'source:chat:web',
                'offline_threading_id': offline_threading_id,
                'message_id': message_id,
                'ephemeral_ttl_mode': '',
                '__user': self.user_id,
                '__a': '1',
                '__req': '1b',
                '__rev': '1015919737',
                'fb_dtsg': self.fb_dtsg
            }

            headers = {
                'Cookie': self.cookie,
                'User-Agent': self.user_agent,
                'Accept': '*/*',
                'Accept-Language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
                'Accept-Encoding': 'gzip, deflate, br',
                'Connection': 'keep-alive',
                'Content-Type': 'application/x-www-form-urlencoded',
                'Origin': 'https://www.facebook.com',
                'Referer': f'https://www.facebook.com/messages/t/{recipient_id}',
                'Host': 'www.facebook.com',
                'Sec-Fetch-Site': 'same-origin',
                'Sec-Fetch-Mode': 'cors',
                'Sec-Fetch-Dest': 'empty'
            }

            try:
                response = requests.post(
                    'https://www.facebook.com/messaging/send/',
                    data=data,
                    headers=headers
                )
                if response.status_code != 200:
                    return {
                        'success': False,
                        'error': 'HTTP_ERROR',
                        'error_description': f'Status code: {response.status_code}'
                    }

                if 'for (;;);' in response.text:
                    clean_text = response.text.replace('for (;;);', '')
                    try:
                        result = json.loads(clean_text)
                        if 'error' in result:
                            return {
                                'success': False,
                                'error': result.get('error'),
                                'error_description': result.get('errorDescription', 'Unknown error')
                            }
                        return {
                            'success': True,
                            'message_id': message_id,
                            'timestamp': timestamp
                        }
                    except json.JSONDecodeError:
                        pass

                return {
                    'success': True,
                    'message_id': message_id,
                    'timestamp': timestamp
                }
            except Exception as e:
                return {
                    'success': False,
                    'error': 'REQUEST_ERROR',
                    'error_description': str(e)
                }

def format_duration(seconds):
    m, s = divmod(int(seconds), 60)
    h, m = divmod(m, 60)
    d, h = divmod(h, 24)
    parts = []
    if d: parts.append(f"{d} ngày")
    if h: parts.append(f"{h} giờ")
    if m: parts.append(f"{m} phút")
    if s or not parts: parts.append(f"{s} giây")
    return " ".join(parts)

def start_spam(user_id, idbox, cookie, message, delay):
    try:
        messenger = Messenger(cookie)
    except Exception as e:
        return f"Lỗi cookie: {str(e)}"

    def loop_send():
        while (user_id, idbox) in treo_threads:
            success = messenger.gui_tn(idbox, message)
            print(f"Gửi Tin Nhắn {'Thành Công' if success else 'Thất Bại'}")
            time.sleep(delay)

    key = (user_id, idbox)
    thread = threading.Thread(target=loop_send)
    treo_threads[key] = thread
    treo_start_times[key] = time.time()
    messenger_instances[key] = messenger
    thread.start()
    return "Đã bắt đầu gửi tin nhắn."
    
def start_nhay(user_id, idbox, cookie, delay):
    if not os.path.exists("nhay.txt"):
        return "Không tìm thấy file nhay.txt."
    try:
        messenger = Messenger(cookie)
    except Exception as e:
        return f"Lỗi cookie: {str(e)}"

    with open("nhay.txt", "r", encoding="utf-8") as f:
        messages = [line.strip() for line in f if line.strip()]

    if not messages:
        return "File nhay.txt không có nội dung."

    def loop_nhay():
        index = 0
        while (user_id, idbox) in nhay_threads:
            message = messages[index % len(messages)]
            success = messenger.gui_tn(idbox, message)
            print(f"Gửi tin nhắn {'Thành công' if success else 'Thất bại'}")
            time.sleep(delay)
            index += 1

    key = (user_id, idbox)
    thread = threading.Thread(target=loop_nhay)
    nhay_threads[key] = thread
    nhay_start_times[key] = time.time()
    thread.start()
    return "Đã bắt đầu nhây."
    
def start_chui(user_id, idbox, cookie, delay):
    if not os.path.exists("chui.txt"):
        return "Không tìm thấy file chui.txt."
    try:
        messenger = Messenger(cookie)
    except Exception as e:
        return f"Lỗi cookie: {str(e)}"

    with open("chui.txt", "r", encoding="utf-8") as f:
        messages = [line.strip() for line in f if line.strip()]

    if not messages:
        return "File chui.txt không có nội dung."

    def loop_chui():
        index = 0
        while (user_id, idbox) in chui_threads:
            message = messages[index % len(messages)]
            success = messenger.gui_tn(idbox, message)
            print(f"Gửi tin nhắn {'Thành công' if success else 'Thất bại'}")
            time.sleep(delay)
            index += 1

    key = (user_id, idbox)
    thread = threading.Thread(target=loop_chui)
    chui_threads[key] = thread
    chui_start_times[key] = time.time()
    thread.start()
    return "Đã bắt đầu gửi tin nhắn."       
    
def start_codelag(user_id, idbox, cookie, delay):
    if not os.path.exists("codelag.txt"):
        return "Không tìm thấy file codelag.txt."
    try:
        messenger = Messenger(cookie)
    except Exception as e:
        return f"Lỗi cookie: {str(e)}"

    with open("codelag.txt", "r", encoding="utf-8") as f:
        messages = [line.strip() for line in f if line.strip()]

    if not messages:
        return "File codelag.txt không có nội dung."

    def loop_codelag():
        index = 0
        while (user_id, idbox) in codelag_threads:
            message = messages[index % len(messages)]
            success = messenger.gui_tn(idbox, message)
            print(f"Gửi tin nhắn {'Thành công' if success else 'Thất bại'}")
            time.sleep(delay)
            index += 1

    key = (user_id, idbox)
    thread = threading.Thread(target=loop_codelag)
    codelag_threads[key] = thread
    codelag_start_times[key] = time.time()
    thread.start()
    return "Đã bắt đầu spam code lag."      

def start_so(user_id, idbox, cookie, delay):
    if not os.path.exists("so.txt"):
        return "Không tìm thấy file so.txt."
    try:
        messenger = Messenger(cookie)
    except Exception as e:
        return f"Lỗi cookie: {str(e)}"

    with open("so.txt", "r", encoding="utf-8") as f:
        messages = [line.strip() for line in f if line.strip()]

    if not messages:
        return "File so.txt không có nội dung."

    def loop_so():
        index = 0
        while (user_id, idbox) in so_threads:
            message = messages[index % len(messages)]
            success = messenger.gui_tn(idbox, message)
            print(f"Gửi tin nhắn {'Thành công' if success else 'Thất bại'}")
            time.sleep(delay)
            index += 1

    key = (user_id, idbox)
    thread = threading.Thread(target=loop_so)
    so_threads[key] = thread
    so_start_times[key] = time.time()
    thread.start()
    return "Đã bắt đầu gửi tin nhắn."


    
# Chức năng set ngôn treo mess
@bot.command()
async def setngonmess(ctx):
    if ctx.author.id not in admins and ctx.author.id != IDADMIN_GOC:
        return await ctx.send("**[GABI BOT]** Bạn đéo có quyền sử dụng bot này.")
    if not ctx.message.attachments:
        return await ctx.send("**[GABI BOT]** Vui lòng đính kèm file .txt.")
    attachment = ctx.message.attachments[0]
    if not attachment.filename.endswith(".txt"):
        return await ctx.send("**[GABI BOT]** Bot chỉ chấp nhận dạng file .txt")
    path = f"{ctx.author.id}_{attachment.filename}"
    await attachment.save(path)
    await ctx.send(f"**[GABI BOT]** Đã lưu file thành công dưới tên: `{path}`.")

# Chức năng treo ngôn messenger
@bot.command()
async def ngonmess(ctx, idbox: str, cookie: str, filename: str, delay: int):
    if ctx.author.id not in admins and ctx.author.id != IDADMIN_GOC:
        return await ctx.send("**[GABI BOT]** Bạn đéo có quyền sử dụng bot này.")
    filepath = f"{ctx.author.id}_{filename}"
    if not os.path.exists(filepath):
        return await ctx.send("**[GABI BOT]** Không tìm thấy file đã set.")
    with open(filepath, "r", encoding="utf-8") as f:
        message = f.read()
    result = start_spam(ctx.author.id, idbox, cookie, message, delay)
    await ctx.send(result)

# Chức năng dừng treo ngôn messenger
@bot.command()
async def stopngonmess(ctx, idbox: str):
    removed = False
    keys_to_remove = [(uid, ib) for (uid, ib) in treo_threads if uid == ctx.author.id and ib == idbox]
    for key in keys_to_remove:
        treo_threads.pop(key)
        treo_start_times.pop(key)
        messenger_instances.pop(key)
        removed = True
    if removed:
        await ctx.send(f"**[GABI BOT]** Đã dừng các tab treo với idbox: `{idbox}`.")
    else:
        await ctx.send("**[GABI BOT]** Không có tab treo nào.")

# Chức năng xem tab treo ngôn messenger
@bot.command()
async def tabngonmess(ctx):
    msg = "**Danh Sách Tab treo:**\n\n"
    count = 0
    for (uid, ib), start in treo_start_times.items():
        if uid == ctx.author.id:
            uptime = format_duration(time.time() - start)
            msg += f"**{ib}:** {uptime}\n"
            count += 1
    if count == 0:
        msg = "**[GABI BOT]** Bạn không có tab treo nào đang chạy."
    await ctx.send(msg)

# Chức năng thêm admin bot
@bot.command()
async def addadmin(ctx, member: discord.Member):
    if ctx.author.id != IDADMIN_GOC:
        return await ctx.send("**[GABI BOT]** Bạn không có quyền sử dụng lệnh này.")
    if member.id not in admins:
        admins.append(member.id)
        await ctx.send(f"**[GABI BOT]** Đã thêm `{member.name}` vào danh sách admin.")
    else:
        await ctx.send("**[GABI BOT]** Người này đã là admin rồi.")

# Chức năng xóa admin bot
@bot.command()
async def deladmin(ctx, member: discord.Member):
    if ctx.author.id != IDADMIN_GOC:
        return await ctx.send("Bạn không có quyền sử dụng lệnh này.")
    if member.id in admins and member.id != IDADMIN_GOC:
        admins.remove(member.id)
        await ctx.send(f"Đã xoá `{member.name}` khỏi danh sách admin.")
                
        to_remove = [task_id for task_id, info in task_info.items() if info['admin_id'] == member.id]
        for task_id in to_remove:
            if task_id in running_tasks:
                running_tasks[task_id].cancel()
                del running_tasks[task_id]
            del task_info[task_id]
        await ctx.send(f"Đã dừng tất cả các task do `{member.name}` tạo.")
    else:
        await ctx.send("Không thể xoá admin gốc hoặc người này không phải admin.")

# List admin bot
@bot.command()
async def listadmin(ctx):
    embed = discord.Embed(
        title="📜 Danh Sách Admin 📜",
        description="Danh sách các admin hiện tại của bot.",
        color=discord.Color.blue()
    )

    for admin_id in admins:
        try:
            user = await bot.fetch_user(admin_id)
            if admin_id == IDADMIN_GOC:
                embed.add_field(name=f"💢 {user.name}", value="(Admin Gốc)", inline=False)
            else:
                embed.add_field(name=f"💢 {user.name}", value="(Admin)", inline=False)
        except Exception:
            embed.add_field(name=f"💢 {admin_id}", value="(Không tìm được tên)", inline=False)

    await ctx.send(embed=embed)

# Chức năng nhây mess    
@bot.command()
async def nhaymess(ctx, idbox: str, cookie: str, delay: int):
    if ctx.author.id not in admins and ctx.author.id != IDADMIN_GOC:
        return await ctx.send("**[HAWUJ💢]** Bạn đéo có quyền sử dụng bot này.")
    result = start_nhay(ctx.author.id, idbox, cookie, delay)
    await ctx.send(result)

# Chức năng dừng nhây mess
@bot.command()
async def stopnhaymess(ctx, idbox: str):
    key = (ctx.author.id, idbox)
    if key in nhay_threads:
        nhay_threads.pop(key)
        nhay_start_times.pop(key)
        await ctx.send(f"**[HAWUJ💢]** Đã dừng nhây id box `{idbox}`.")
    else:
        await ctx.send("**[HAWUJ💢]** Không có lệnh nhây nào đang chạy.")

# Chức năng xem tab nhây mess
@bot.command()
async def tabnhaymess(ctx):
    msg = "**Danh Sách Tab nhây:**\n\n"
    count = 0
    for (uid, ib), start in nhay_start_times.items():
        if uid == ctx.author.id:
            uptime = format_duration(time.time() - start)
            msg += f"**{ib}:** {uptime}\n"
            count += 1
    if count == 0:
        msg = "**[GABI BOT]** Bạn không có tab nhây nào đang chạy."
    await ctx.send(msg) 

# Chức năng chửi đổng mess
@bot.command()
async def ideamess(ctx, idbox: str, cookie: str, delay: int):
    if ctx.author.id not in admins and ctx.author.id != IDADMIN_GOC:
        return await ctx.send("**[HAWUJ💢]** Bạn đéo có quyền sử dụng bot này.")
    result = start_chui(ctx.author.id, idbox, cookie, delay)
    await ctx.send(result)

# Chức năng dừng chửi đổng mess
@bot.command()
async def stopideamess(ctx, idbox: str):
    key = (ctx.author.id, idbox)
    if key in chui_threads:
        chui_threads.pop(key)
        chui_start_times.pop(key)
        await ctx.send(f"**[HAWUJ💢]** Đã dừng chửi id box `{idbox}`.")
    else:
        await ctx.send("**[HAWUJ💢]** Không có lệnh chửi nào đang chạy.")

# Chức năng xem tab chửi mess
@bot.command()
async def tabideamess(ctx):
    msg = "**Danh Sách Tab:**\n\n"
    count = 0
    for (uid, ib), start in chui_start_times.items():
        if uid == ctx.author.id:
            uptime = format_duration(time.time() - start)
            msg += f"**{ib}:** {uptime}\n"
            count += 1
    if count == 0:
        msg = "**[HAWUJ💢]** Bạn không có tab nào đang chạy."
    await ctx.send(msg)

# Chức năng spam codelag mess    
@bot.command()
async def codelag(ctx, idbox: str, cookie: str, delay: int):
    if ctx.author.id not in admins and ctx.author.id != IDADMIN_GOC:
        return await ctx.send("**[HAWUJ💢]** Bạn đéo có quyền sử dụng bot này.")
    result = start_codelag(ctx.author.id, idbox, cookie, delay)
    await ctx.send(result)

# Chức năng dừng codelag mess             
@bot.command()
async def stopcodelag(ctx, idbox: str):
    key = (ctx.author.id, idbox)
    if key in codelag_threads:
        codelag_threads.pop(key)
        codelag_start_times.pop(key)
        await ctx.send(f"**[HAWUJ💢]** Đã dừng spam code lag vào {idbox}.")
    else:
        await ctx.send("**[HAWUJ💢]** Không có tab code lag nào đang chạy.")

# Chức năng xem tab codelag mess   
@bot.command()
async def tabcodelag(ctx):
    msg = "**Danh Sách Tab code lag:**\n\n"
    count = 0
    for (uid, ib), start in codelag_start_times.items():
        if uid == ctx.author.id:
            uptime = format_duration(time.time() - start)
            msg += f"**{ib}:** {uptime}\n"
            count += 1
    if count == 0:
        msg = "**[HAWUJ💢]** Bạn không có tab code lag nào đang chạy."
    await ctx.send(msg)

# Chức năng thả sớ mess
@bot.command()
async def so(ctx, idbox: str, cookie: str, delay: int):
    if ctx.author.id not in admins and ctx.author.id != IDADMIN_GOC:
        return await ctx.send("**[HAWUJ💢]** Bạn đéo có quyền sử dụng bot này.")
    result = start_so(ctx.author.id, idbox, cookie, delay)
    await ctx.send(result)

# Chức năng dừng thả sớ mess             
@bot.command()
async def stopso(ctx, idbox: str):
    key = (ctx.author.id, idbox)
    if key in so_threads:
        so_threads.pop(key)
        so_start_times.pop(key)
        await ctx.send(f"**[HAWUJ💢]** Đã dừng thả sớ vào {idbox}.")
    else:
        await ctx.send("**[HAWUJ💢]** Không có tab sớ nào đang chạy.")

# Chức năng xem tab sớ mess   
@bot.command()
async def tabso(ctx):
    msg = "**Danh Sách Tab Sớ:**\n\n"
    count = 0
    for (uid, ib), start in so_start_times.items():
        if uid == ctx.author.id:
            uptime = format_duration(time.time() - start)
            msg += f"**{ib}:** {uptime}\n"
            count += 1
    if count == 0:
        msg = "**[HAWUJ💢]** Bạn không có tab sớ nào đang chạy."
    await ctx.send(msg)
    
# Menu trang xịn - code bởi Ares
class SimpleMenu(discord.ui.View):
    def __init__(self):
        super().__init__()
        
        self.items = [ 
            ("⚙️ .menu", "Xem các chức năng của bot"),
            ("💢 .uptime", "Xem thời gian bot hoạt động"),
            ("💢 .ping", "Kiểm tra độ trễ của bot"),
            ("💢 .idkenh", "Lấy id kênh"),
            ("💢 .idsv", "Lấy id máy chủ"),
            ("💢 .ngonmess [idbox] [cookie] [file.txt] [delay]", "Treo ngôn mess"),
            ("💢 .nhaymess [idbox] [cookie] [delay]", "Nhây mess"),
            ("💢 .ideamess [idbox] [cookie] [delay]", "Chửi đổng mess"),
            ("💢 .so [idbox] [cookie] [delay]", "Thả sớ mess"),
            ("💢 .codelag [idbox] [cookie] [delay]", "Codelag mess"),
            ("⛔ .stop [Lệnh war] [idbox]", "Dừng lệnh war đang chạy"),
            ("📤 .setngonmess [Gửi kèm file .txt]", "Set ngôn cho treo mess"),
            ("🔒 .addadmin [@user]", "Thêm người dùng làm admin"),
            ("🔓 .deladmin [@user]", "Xóa admin của người dùng"),
            ("📂 .tab [Lệnh war]", "Xem các task đang chạy"),
            ("💢 .reo [Idbox] [Cookie] [Delay]","Nhây Tag Mess"),
            ("💢 .stopreo [Idbox] [Cookie] [Delay]","Stop Nhây Tag Mess"),
            ("💢 .nhaytop [Cookie] [Delay]","Nhây Bài Viết"),
            ("💢 .stopnhaytop","Stop Nhây Bài Viết"), 
            ("💢 .spam [nội dung]", "Spam nội dung"),
            ("💢 .nhay [id kênh] [delay]", "Nhây discord nhiều kênh"),
            ("🛑 .stopspam", "Dừng tất cả task spam"),
            ("🛑 .stopnhay [id kênh]", "Không id kênh thì dừng all task nhây"),                                   
        ]
        
        self.per_page = 10
        self.pages = self.build_pages()
        self.total = len(self.pages)
        self.current = 0

    def build_pages(self):
        pages = []
        titles = [
    "🛸 TIỆN ÍCH DISCORD 🛸",  
    "🧸 CHỨC NĂNG MESSENGER 🧸",  
    "🌟 CHỨC NĂNG DISCORD 🌟" 
]
        
        for i in range(0, len(self.items), self.per_page):
            chunk = self.items[i:i+self.per_page]
            page_number = len(pages) + 1
            embed = discord.Embed(
                title=titles[page_number - 1] if page_number <= len(titles) else "Trang khác",
                color=discord.Color.red()
            )
            for title, desc in chunk:
                embed.add_field(name=title, value=desc, inline=False)
            embed.set_footer(text=f"Trang {page_number}/{(len(self.items)-1)//self.per_page + 1}")
            pages.append(embed)
        
        return pages

    @discord.ui.button(label="⬅️", style=discord.ButtonStyle.secondary)
    async def previous(self, interaction: discord.Interaction, button: discord.ui.Button):
        if self.current > 0:
            self.current -= 1
            await interaction.response.edit_message(embed=self.pages[self.current], view=self)

    @discord.ui.button(label="➡️", style=discord.ButtonStyle.secondary)
    async def next(self, interaction: discord.Interaction, button: discord.ui.Button):
        if self.current < self.total - 1:
            self.current += 1
            await interaction.response.edit_message(embed=self.pages[self.current], view=self)

@bot.command()
async def menu(ctx):	
    view = SimpleMenu()
    msg = await ctx.send(embed=view.pages[0], view=view)
    await asyncio.sleep(300)
    try:
        await msg.delete()
    except discord.NotFound:
        pass

@bot.command()
async def ping(ctx):
    latency = bot.latency * 1000

    embed = discord.Embed(
        title="[HAWUJ💢] Ping Bot",
        color=discord.Color.green()
    )

    embed.add_field(
        name="Độ trễ hiện tại",
        value=f"> `{latency:.2f} ms`",
        inline=False
    )

    embed.set_footer(
        text=f"Yêu cầu bởi {ctx.author.display_name}",
        icon_url=ctx.author.avatar.url if ctx.author.avatar else None
    )

    await ctx.send(embed=embed)

@bot.command()
async def stopnhaytop(ctx):
    if ctx.author.id not in admins:
        return await ctx.send("Bạn không có quyền sử dụng lệnh này.")

    admin_task_count = {}
    for task_id, info in task_info.items():
        if task_id.startswith("nhaytop_"):
            admin_id = info['admin_id']
            admin_task_count[admin_id] = admin_task_count.get(admin_id, 0) + 1

    if not admin_task_count:
        return await ctx.send("Hiện không có task nhaytop nào chạy.")

    admin_list = list(admin_task_count.items())
    msg = "**Danh sách admin đang có task nhaytop:**\n"
    for i, (admin_id, count) in enumerate(admin_list, start=1):
        try:
            user = await bot.fetch_user(admin_id)
            msg += f"{i}. Admin {user.mention} đã tạo {count} task.\n"
        except:
            msg += f"{i}. Admin ID {admin_id} đã tạo {count} task.\n"

    msg += "\nNhập số (ví dụ: 1, 2) để xem task của admin tương ứng."
    await ctx.send(msg)

    def check(m):
        return m.author == ctx.author and m.channel == ctx.channel

    try:
        reply = await bot.wait_for('message', timeout=30.0, check=check)
        index = int(reply.content.strip()) - 1
        if index < 0 or index >= len(admin_list):
            return await ctx.send("Số không hợp lệ.")

        selected_admin_id = admin_list[index][0]
        if selected_admin_id != ctx.author.id:
            return await ctx.send("Bạn chỉ có thể dừng task do chính mình tạo.")

        tasks = []
        task_mapping = {}
        for task_id, info in task_info.items():
            if info['admin_id'] == selected_admin_id and task_id.startswith("nhaytop_"):
                post_id = info['post_id']
                group_id = info['group_id']
                start_time = info['start_time']
                delta = datetime.now() - datetime.fromtimestamp(start_time)
                formatted_time = str(delta).split('.')[0]
                task_index = len(tasks) + 1
                tasks.append(f"{task_index}. Group ID: {group_id}, Post ID: {post_id} (chạy được {formatted_time})")
                task_mapping[task_index] = task_id

        if not tasks:
            return await ctx.send("Admin này không có task nhaytop nào.")

        await ctx.send("**Danh sách task của admin đã chọn:**\n" + "\n".join(tasks) + "\n\nNhập số task để dừng (ví dụ: 1, 2) hoặc 'all' để dừng tất cả.")

        reply = await bot.wait_for('message', timeout=30.0, check=check)
        user_input = reply.content.strip().lower()

        if user_input == "all":
            stopped_tasks = []
            for task_index, task_id in task_mapping.items():
                running_tasks[task_id].cancel()
                start_time = task_info[task_id]['start_time']
                delta = datetime.now() - datetime.fromtimestamp(start_time)
                formatted_time = str(delta).split('.')[0]
                group_id = task_info[task_id]['group_id']
                post_id = task_info[task_id]['post_id']
                stopped_tasks.append(f"Task Group ID: {group_id}, Post ID: {post_id} (chạy được {formatted_time})")
                del running_tasks[task_id]
                del task_info[task_id]
            await ctx.send(f"Đã dừng tất cả task:\n" + "\n".join(stopped_tasks))
        else:
            task_index = int(user_input)
            if task_index not in task_mapping:
                return await ctx.send("Số task không hợp lệ.")
            
            task_id = task_mapping[task_index]
            running_tasks[task_id].cancel()
            start_time = task_info[task_id]['start_time']
            delta = datetime.now() - datetime.fromtimestamp(start_time)
            formatted_time = str(delta).split('.')[0]
            group_id = task_info[task_id]['group_id']
            post_id = task_info[task_id]['post_id']
            del running_tasks[task_id]
            del task_info[task_id]
            await ctx.send(f"Đã dừng task Group ID: `{group_id}`, Post ID: `{post_id}` (chạy được {formatted_time}).")

    except asyncio.TimeoutError:
        await ctx.send("Hết thời gian chờ, vui lòng thử lại sau.")
    except ValueError:
        await ctx.send("Vui lòng nhập số hợp lệ hoặc 'all'.")
    except Exception as e:
        await ctx.send(f"Đã xảy ra lỗi: {str(e)}")

@bot.command()
async def uptime(ctx):
    now = datetime.datetime.utcnow()
    delta = now - start_time
    total_seconds = int(delta.total_seconds())

    seconds = total_seconds % 60
    minutes = (total_seconds // 60) % 60
    hours = (total_seconds // 3600) % 24
    days = (total_seconds // 86400) % 7
    weeks = (total_seconds // 604800) % 4
    months = (total_seconds // 2592000) % 12  
    years = total_seconds // 31536000          

    embed = discord.Embed(
        title="[GABI BOT] Uptime Bot",
        color=discord.Color.blue()
    )

    embed.add_field(name="Thời gian hoạt động", value="\n".join([
        f"> `{years}` năm",
        f"> `{months}` tháng",
        f"> `{weeks}` tuần",
        f"> `{days}` ngày",
        f"> `{hours}` giờ",
        f"> `{minutes}` phút",
        f"> `{seconds}` giây",
    ]), inline=False)

    embed.set_footer(
        text=f"Yêu cầu bởi {ctx.author.display_name}",
        icon_url=ctx.author.avatar.url if ctx.author.avatar else None
    )

    await ctx.send(embed=embed)

# lấy id kênh và id server
@bot.command()
async def idkenh(ctx):
    if ctx.author.id not in admins and ctx.author.id != IDADMIN_GOC:
        return await ctx.send("**[GABI BOT]** Bạn đéo có quyền sử dụng lệnh này.")
    await ctx.send(f'Channel ID: {ctx.channel.id}')
@bot.command()
async def idsv(ctx):
    if ctx.author.id not in admins and ctx.author.id != IDADMIN_GOC:
        return await ctx.send("**[GABI BOT]** Bạn đéo có quyền sử dụng lệnh này.")    
    await ctx.send(f'Server ID: {ctx.guild.id}')

spamming_tasks = []

@bot.command()
async def spam(ctx, ids: str, delay: int, *, content: str):
    if ctx.author.id not in admins and ctx.author.id != IDADMIN_GOC:
        return await ctx.send("**[GABI BOT]** Bạn đéo có quyền sử dụng lệnh này.")
    
    channel_ids = [int(id.strip()) for id in ids.split(",")]

    async def spam_channel(channel_id):
        try:
            channel = bot.get_channel(channel_id)
            if channel:
                while True:
                    await channel.send(content)
                    await asyncio.sleep(delay)
        except Exception as e:
            print(f"Lỗi khi spam kênh {channel_id}: {e}")

    for cid in channel_ids:
        task = bot.loop.create_task(spam_channel(cid))
        spamming_tasks.append(task)

    await ctx.send("**[GABI BOT]** Đã bắt đầu spam.")

@bot.command()
async def stopspam(ctx):
    if ctx.author.id not in admins and ctx.author.id != IDADMIN_GOC:
        return await ctx.send("Bạn đéo có quyền sử dụng lệnh này.")
    
    for task in spamming_tasks:
        task.cancel()
    spamming_tasks.clear()
    await ctx.send("**[GABI BOT]** Đã dừng tất cả spam.")

nhay_tasks = {}

@bot.command()
async def nhay(ctx, channel_ids: str, delay: int):
    channels = [bot.get_channel(int(channel_id.strip())) for channel_id in channel_ids.split(",")]

    try:
        with open("nhay.txt", "r", encoding="utf-8") as file:
            lines = file.readlines()
    except FileNotFoundError:
        return await ctx.send("**[GABI BOT]** Không tìm thấy file nhay.txt.")

    async def nhay_in_channel(channel):
        while True:
            for line in lines:
                await channel.send(line.strip())
                await asyncio.sleep(delay)

    for channel in channels:
        if channel.id not in nhay_tasks:
            nhay_task = bot.loop.create_task(nhay_in_channel(channel))
            nhay_tasks[channel.id] = nhay_task
        else:
            await ctx.send(f"**[GABI BOT]** Đang có task nhay cho kênh {channel.name}.")

    await ctx.send(f"**[GABI BOT]** Đã bắt đầu nhay cho các kênh: {', '.join([channel.name for channel in channels])}.")
    
    
@bot.command()
async def reo(ctx, id_box: str, cookie: str, delay: float):
    if ctx.author.id not in admins:
        return await ctx.send("Bạn không có quyền sử dụng lệnh này.")
    
    # Kiểm tra file nhay.txt
    file_path = "nhay.txt"
    if not os.path.exists(file_path):
        return await ctx.send("File `nhay.txt` không tồn tại.")

    # Yêu cầu nhập ID người cần tag
    await ctx.send("Vui lòng nhập ID người cần tag:")

    def check(m):
        return m.author == ctx.author and m.channel == ctx.channel

    try:
        msg = await bot.wait_for('message', timeout=30.0, check=check)
        tagged_id = msg.content.strip()
        if not tagged_id.isdigit():
            return await ctx.send("ID tag phải là số hợp lệ.")
    except asyncio.TimeoutError:
        return await ctx.send("Hết thời gian chờ nhập ID tag.")

    # Kiểm tra cookie và lấy fb_dtsg, jazoest
    fb_dtsg, jazoest = get_fb_dtsg_jazoest(cookie, id_box)
    if not fb_dtsg:
        return await ctx.send("Cookie không hợp lệ hoặc không lấy được thông tin.")

    # Đọc nội dung từ nhay.txt
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = [line.strip() for line in f if line.strip()]
    if not lines:
        return await ctx.send("File `nhay.txt` rỗng, vui lòng thêm nội dung.")

    # Tạo task ID duy nhất
    task_id = f"reo_{id_box}_{time.time()}"
    
    async def spam_reo():
        index = 0
        while True:
            # Tạo nội dung tin nhắn với tag người dùng
            content = f"{lines[index]} @[tagged_id:0]"
            success = send_message(id_box, fb_dtsg, jazoest, cookie, content)
            if success:
                print(f"[+] Đã gửi tin nhắn với tag vào box {id_box}: {content}")
            else:
                print(f"[!] Gửi tin nhắn thất bại vào box {id_box}")
            index = (index + 1) % len(lines)
            await asyncio.sleep(delay)

    # Tạo và lưu task
    task = asyncio.create_task(spam_reo())
    running_tasks[task_id] = task
    task_info[task_id] = {
        'admin_id': ctx.author.id,
        'start_time': time.time(),
        'tagged_id': tagged_id,
        'box_id': id_box
    }
    await ctx.send(f"Đã bắt đầu `reo` vào box `{id_box}` và tag ID `{tagged_id}` với tốc độ `{delay}` giây.")

@bot.command()
async def stopreo(ctx, id_box: str):
    if ctx.author.id not in admins:
        return await ctx.send("Bạn không có quyền sử dụng lệnh này.")
    
    # Tìm tất cả task liên quan đến id_box
    tasks_to_stop = [task_id for task_id in running_tasks if task_id.startswith(f"reo_{id_box}")]
    
    if not tasks_to_stop:
        return await ctx.send(f"Không có task `reo` nào đang chạy cho box `{id_box}`.")
    
    for task_id in tasks_to_stop:
        if task_info.get(task_id, {}).get('admin_id') == ctx.author.id or ctx.author.id == IDADMIN_GOC:
            running_tasks[task_id].cancel()
            tagged_id = task_info[task_id].get('tagged_id', 'Unknown')
            del running_tasks[task_id]
            del task_info[task_id]
            await ctx.send(f"Đã dừng lệnh `reo` trong box `{id_box}` với tag ID `{tagged_id}`.")
        else:
            await ctx.send(f"Bạn không có quyền dừng task `{task_id}`.")
            

@bot.command()
async def stopnhay(ctx, channel_id: str = None):
    if channel_id:
        channel = bot.get_channel(int(channel_id))
        if channel and channel.id in nhay_tasks:
            nhay_tasks[channel.id].cancel()
            del nhay_tasks[channel.id]
            await ctx.send(f"**[GABI BOT]** Đã dừng nhay cho kênh {channel.name}.")
        else:
            await ctx.send("**[GABI BOT]** Không tìm thấy task nhay cho kênh này.")
    else:
        for task in nhay_tasks.values():
            task.cancel()
        nhay_tasks.clear()
        await ctx.send("**[GABI BOT]** Đã dừng tất cả các task nhay.")

def get_guid():
    section_length = int(time.time() * 1000)
    
    def replace_func(c):
        nonlocal section_length
        r = (section_length + random.randint(0, 15)) % 16
        section_length //= 16
        return hex(r if c == "x" else (r & 7) | 8)[2:]

    return "".join(replace_func(c) if c in "xy" else c for c in "xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx")

def normalize_cookie(cookie, domain='www.facebook.com'):
    headers = {
        'Cookie': cookie,
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (like Gecko) Chrome/122.0.0.0 Safari/537.36'
    }
    try:
        response = requests.get(f'https://{domain}/', headers=headers, timeout=10)
        if response.status_code == 200:
            set_cookie = response.headers.get('Set-Cookie', '')
            new_tokens = re.findall(r'([a-zA-Z0-9_-]+)=[^;]+', set_cookie)
            cookie_dict = dict(re.findall(r'([a-zA-Z0-9_-]+)=([^;]+)', cookie))
            for token in new_tokens:
                if token not in cookie_dict:
                    cookie_dict[token] = ''
            return ';'.join(f'{k}={v}' for k, v in cookie_dict.items() if v)
    except:
        pass
    return cookie
    
def get_uid_fbdtsg(ck):
    try:
        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'en-US,en;q=0.9,vi;q=0.8',
            'Connection': 'keep-alive',
            'Cookie': ck,
            'Host': 'www.facebook.com',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'none',
            'Sec-Fetch-User': '?1',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (like Gecko) Chrome/122.0.0.0 Safari/537.36'
        }
        
        try:
            response = requests.get('https://www.facebook.com/', headers=headers)
            
            if response.status_code != 200:
                print(f"Status Code >> {response.status_code}")
                return None, None, None, None, None, None
                
            html_content = response.text
            
            user_id = None
            fb_dtsg = None
            jazoest = None
            
            script_tags = re.findall(r'<script id="__eqmc" type="application/json[^>]*>(.*?)</script>', html_content)
            for script in script_tags:
                try:
                    json_data = json.loads(script)
                    if 'u' in json_data:
                        user_param = re.search(r'__user=(\d+)', json_data['u'])
                        if user_param:
                            user_id = user_param.group(1)
                            break
                except:
                    continue
            
            fb_dtsg_match = re.search(r'"f":"([^"]+)"', html_content)
            if fb_dtsg_match:
                fb_dtsg = fb_dtsg_match.group(1)
            
            jazoest_match = re.search(r'jazoest=(\d+)', html_content)
            if jazoest_match:
                jazoest = jazoest_match.group(1)
            
            revision_match = re.search(r'"server_revision":(\d+),"client_revision":(\d+)', html_content)
            rev = revision_match.group(1) if revision_match else ""
            
            a_match = re.search(r'__a=(\d+)', html_content)
            a = a_match.group(1) if a_match else "1"
            
            req = "1b"
                
            return user_id, fb_dtsg, rev, req, a, jazoest
                
        except requests.exceptions.RequestException as e:
            print(f"Lỗi Kết Nối Khi Lấy UID/FB_DTSG: {e}")
            return get_uid_fbdtsg(ck)
            
    except Exception as e:
        print(f"Lỗi: {e}")
        return None, None, None, None, None, None

def get_info(uid: str, cookie: str, fb_dtsg: str, a: str, req: str, rev: str) -> Dict[str, Any]:
    try:
        form = {
            "ids[0]": uid,
            "fb_dtsg": fb_dtsg,
            "__a": a,
            "__req": req,
            "__rev": rev
        }
        
        headers = {
            'Accept': '*/*',
            'Accept-Language': 'en-US,en;q=0.9,vi;q=0.8',
            'Connection': 'keep-alive',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Cookie': cookie,
            'Origin': 'https://www.facebook.com',
            'Referer': 'https://www.facebook.com/',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (like Gecko) Chrome/122.0.0.0 Safari/537.36'
        }
        
        response = requests.post(
            "https://www.facebook.com/chat/user_info/",
            headers=headers,
            data=form
        )
        
        if response.status_code != 200:
            return {"error": f"Lỗi Kết Nối: {response.status_code}"}
        
        try:
            text_response = response.text
            if text_response.startswith("for (;;);"):
                text_response = text_response[9:]
            
            res_data = json.loads(text_response)
            
            if "error" in res_data:
                return {"error": res_data.get("error")}
            
            if "payload" in res_data and "profiles" in res_data["payload"]:
                return format_data(res_data["payload"]["profiles"])
            else:
                return {"error": f"Không Tìm Thấy Thông Tin Của {uid}"}
                
        except json.JSONDecodeError:
            return {"error": "Lỗi Khi Phân Tích JSON"}
            
    except Exception as e:
        print(f"Lỗi Khi Get Info: {e}")
        return {"error": str(e)}

def format_data(profiles):
    if not profiles:
        return {"error": "Không Có Data"}
    
    first_profile_id = next(iter(profiles))
    profile = profiles[first_profile_id]
    
    return {
        "id": first_profile_id,
        "name": profile.get("name", ""),
        "url": profile.get("url", ""),
        "thumbSrc": profile.get("thumbSrc", ""),
        "gender": profile.get("gender", "")
    }

def cmt_gr_pst(cookie, grid, postIDD, ctn, user_id, fb_dtsg, rev, req, a, jazoest, uidtag=None, nametag=None):
    try:
        if not all([user_id, fb_dtsg, jazoest]):
            print("Thiếu user_id, fb_dtsg hoặc jazoest")
            return False
        client_mutation_id = str(round(random.random() * 19))
        session_id = get_guid()  
        crt_time = int(time.time() * 1000)
        
        variables = {
            "feedLocation": "DEDICATED_COMMENTING_SURFACE",
            "feedbackSource": 110,
            "groupID": grid,
            "input": {
                "client_mutation_id": client_mutation_id,
                "actor_id": user_id,
                "attachments": None,
                "feedback_id": pstid_enc,
                "formatting_style": None,
                "message": {
                    "ranges": [],
                    "text": ctn
                },
                "attribution_id_v2": f"SearchCometGlobalSearchDefaultTabRoot.react,comet.search_results.default_tab,tap_search_bar,{crt_time},775647,391724414624676,,",
                "vod_video_timestamp": None,
                "is_tracking_encrypted": True,
                "tracking": [],
                "feedback_source": "DEDICATED_COMMENTING_SURFACE",
                "session_id": session_id
            },
            "inviteShortLinkKey": None,
            "renderLocation": None,
            "scale": 3,
            "useDefaultActor": False,
            "focusCommentID": None,
            "__relay_internal__pv__IsWorkUserrelayprovider": False
        }
        
        if uidtag and nametag:
            name_position = ctn.find(nametag)
            if name_position != -1:
                variables["input"]["message"]["ranges"] = [
                    {
                        "entity": {
                            "id": uidtag
                        },
                        "length": len(nametag),
                        "offset": name_position
                    }
                ]
            
        payload = {
            'av': user_id,
            '__crn': 'comet.fbweb.CometGroupDiscussionRoute',
            'fb_dtsg': fb_dtsg,
            'jazoest': jazoest,
            'fb_api_caller_class': 'RelayModern',
            'fb_api_req_friendly_name': 'useCometUFICreateCommentMutation',
            'variables': json.dumps(variables),
            'server_timestamps': 'true',
            'doc_id': '24323081780615819'
        }
        
        headers = {
            'Accept': '*/*',
            'Accept-Encoding': 'identity',
            'Connection': 'keep-alive',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Cookie': cookie,
            'Origin': 'https://www.facebook.com',
            'Referer': f'https://www.facebook.com/groups/{grid}',
            'User-Agent': 'python-http/0.27.0'
        }
        
        response = requests.post('https://www.facebook.com/api/graphql', data=payload, headers=headers)
        print(f"Mã trạng thái cho bài {postIDD}: {response.status_code}")
        print(f"Phản hồi: {response.text[:500]}...") 
        
        if response.status_code == 200:
            try:
                json_response = response.json()
                if 'errors' in json_response:
                    print(f"Lỗi GraphQL: {json_response['errors']}")
                    return False
                if 'data' in json_response and 'comment_create' in json_response['data']:
                    print("Bình luận đã được đăng")
                    return True
                print("Không tìm thấy comment_create trong phản hồi")
                return False
            except ValueError:
                print("Phản hồi JSON không hợp lệ")
                return False
        else:
            return False
    except Exception as e:
        print(f"Lỗi khi gửi bình luận: {e}")
        return False

def extract_post_group_id(post_link):
    post_match = re.search(r'facebook\.com/.+/permalink/(\d+)', post_link)
    group_match = re.search(r'facebook\.com/groups/(\d+)', post_link)
    if not post_match or not group_match:
        return None, None
    return post_match.group(1), group_match.group(1)

@bot.command()
async def nhaytop(ctx, cookie: str, delay: float):
    if ctx.author.id not in admins and ctx.author.id != IDADMIN_GOC:
        await ctx.send("**[GABI BOT]** Bạn đéo có quyền sử dụng bot này.")
        return

    path = "nhay.txt"
    if not os.path.exists(path):
        await ctx.send("Không tìm thấy file `nhay.txt`.")
        return

    await ctx.send("Vui lòng nhập link bài viết (ví dụ: https://facebook.com/groups/123/permalink/456):")
    def check(m):
        return m.author == ctx.author and m.channel == ctx.channel
    try:
        msg = await bot.wait_for('message', timeout=30.0, check=check)
        post_link = msg.content.strip()
    except asyncio.TimeoutError:
        await ctx.send("Hết thời gian chờ nhập link bài viết.")
        return

    post_id, group_id = extract_post_group_id(post_link)
    if not post_id or not group_id:
        await ctx.send("Link bài viết không hợp lệ hoặc không tìm được group_id.")
        return

    cookie = normalize_cookie(cookie)
    
    user_id, fb_dtsg, rev, req, a, jazoest = get_uid_fbdtsg(cookie)
    if not user_id or not fb_dtsg or not jazoest:
        await ctx.send("Cookie không hợp lệ hoặc không lấy được thông tin.")
        return

    with open(path, 'r', encoding='utf-8') as f:
        lines = [line.strip() for line in f if line.strip()]
    if not lines:
        await ctx.send("File `nhay.txt` rỗng.")
        return

    task_id = f"nhaytop_{post_id}_{time.time()}"
    
    async def loop_nhaytop():
        index = 0
        while True:
            message = lines[index]
            success = cmt_gr_pst(cookie, group_id, post_id, message, user_id, fb_dtsg, rev, req, a, jazoest)
            if success:
                print(f"[+] Đã gửi bình luận vào bài {post_id}: {message}")  
            else:
                print(f"[!] Gửi bình luận thất bại vào bài {post_id}")  
            index = (index + 1) % len(lines)
            await asyncio.sleep(delay)

    task = asyncio.create_task(loop_nhaytop())
    running_tasks[task_id] = task
    task_info[task_id] = {
        'admin_id': ctx.author.id,
        'start_time': time.time(),
        'post_id': post_id,
        'group_id': group_id
    }
    await ctx.send(f"Đã bắt đầu `nhaytop` vào bài viết `{post_id}` với tốc độ `{delay}` giây.")
bot.run(TOKEN)