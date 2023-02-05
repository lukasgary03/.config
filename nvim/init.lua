vim.g.loaded_netrw = 1
vim.g.loaded_netrwPlugin = 1
require("luke.set")
require("luke.packer-plugins")
require("luke.keymap")

vim.g.mapleader = " "

--vim.api.nvim_set_keymap('i', 'jk', '<ESC>', { noremap = true})
