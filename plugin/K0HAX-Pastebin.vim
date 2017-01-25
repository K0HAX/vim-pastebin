if !has('python3') && !has('python')
    finish
endif

let s:path = fnamemodify(resolve(expand('<sfile>:p')), ':h:h') . '/pastebin.py'
let s:path3 = fnamemodify(resolve(expand('<sfile>:p')), ':h:h') . '/pastebin3.py'

function! s:K0HAXPastebin(mLanguage)
    if has('python')
        execute 'pyfile ' . s:path
    elseif has('python3')
        execute 'py3file ' . s:path3
    end
endfunc

command! -nargs=1 Pastebin call s:K0HAXPastebin(<f-args>)

