m_start = '<b>Hai!🙂, Selamat datang di Anonim Chat Polines</b>\n'

m_is_not_free_users = 'Sedang mencari lawan bicara.. 😊'

m_is_connect = 'Partner ditemukan, say "Hay \U0001F44B"'\

m_play_again = 'Ingin mengobrol dengan orang lain?'

m_is_not_user_name = 'Maaf, tetapi di bot kami, komunikasi hanya dapat dilakukan jika Anda memiliki nama pengguna'

m_good_bye = 'Bot berhenti, klik Mulai untuk memulai kembali'

m_disconnect_user = '🙂 ouch..! Dia pergi'

m_failed = '🙂 Telah terjadi kesalahan!'

m_like = ' 😋 Pilihan bagus!'

m_dislike_user = '🙂 Dialog berakhir'

m_dislike_user_to = ' 😓Teman bicara tidak menyukaimu, maaf'

m_send_some_messages = '😊 Anda tidak dapat meneruskan pesan Anda sendiri'

m_has_not_dialog = 'Anda tidak dalam dialog'

m_success_sharelink = 'Profile mu sudah terkirim'

m_bantuan = '  <b>Bot Bantuan</b> \n\n'\
    '\U000025B6 <b>Mulai Bot = </b> <code>untuk memulai bot</code>\n\n'\
    '\U0001F50D <b>Cari Partner = </b> <code>Mencari partner</code>\n\n'\
    '\U000023E9 <b>Next = </b> <code>Menghentikan dialog dan mencari partner baru</code>\n\n'\
    '\U000026D4 <b>Berhenti = </b> <code>Menghentikan dialog</code>\n\n'\
    '🤝 <b>Share Profile = </b> <code>mengirimkan username Telegram ke partner</code>\n\n'\
    '\U0001F4BB <b>Bantuan = </b> <code>Cara menggunakan bot</code>\n\n'\
    '\U0001F6A7 <b>Rules = </b> <code>Aturan penggunaan bot</code>\n\n'\

m_rules = '<b>Rules - Anonim Bot </b>\n\n' \
          '<i>Menggunakan bot ini berarti menaati aturan yaa..</i>\n\n'\
          '1.Bot Anonim ini tidak menyimpan data diri pribadi, semua isi chat disimpan dalam akun telegram masing-masing\n\n'\
          '2.Dilarang Keras mengirimkan <b> DATA PRIBADI, PASSWORD, DSB </b>, admin tidak akan bertanggung jawab atas apa yang bagikan.\n\n' \
          '3.Gunakanlah Bahasa yang Sopan\n\n'\
          '4.Dilarang berbagi hal yang berkaitan dengan HOAX maupun SARA.\n\n'\
          '5.Diskusi Seputar Bot bisa di Grup <i>Link ada di deskripsi</i>\n\n'\
          'Jika Melanggar Rules Maka Akan Kami Banned, Aturan ini dapat berubah sesuai keadaan\n'\
          'Selamat Berchatting Anonim'

stop_str = '\U000026D4 Berhenti'

new_str = '\U00002709 New Chat'

skip_str = '\U000023E9 Next'

cari_str = '\U0001F50D Cari Partner'

sharelink_str = '🤝 Share Profile'

rules_str = '\U0001F6A7 Rules'

bantuan_str = '\U0001F4BB Bantuan'

start_str = '\U000025B6 Mulai Bot'

def m_sharelink(x):
    return ('Hai.. kamu dapat profile partner kamu loh \n Nama usernamenya @' + str(x) + '\n')
