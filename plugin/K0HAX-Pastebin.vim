if !has('python')
    finish
endif

function! s:K0HAXPastebin(mLanguage)
    pyfile globpath(&rtp, 'python/pastebin.py')
endfunc

command! -nargs=1 Pastebin call s:K0HAXPastebin(<f-args>)

