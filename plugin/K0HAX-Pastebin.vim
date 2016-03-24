if !has('python')
    finish
endif

let s:path = fnamemodify(resolve(expand('<sfile>:p')), ':h:h') . '/pastebin.py'

function! s:K0HAXPastebin(mLanguage)
    execute 'pyfile ' . s:path
endfunc

command! -nargs=1 Pastebin call s:K0HAXPastebin(<f-args>)

