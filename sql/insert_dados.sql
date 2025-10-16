-- Inserir leitores
INSERT INTO leitor (nome, cpf, telefone, email)
VALUES
("Marcelo Mindas", "180.081.097-00", "27 99659-2133", "mindasmarcelo@gmail.com");

-- Inserir livros
INSERT INTO Livro (titulo, autor, editora, categoria, quantidade)
VALUES
('Dom Casmurro', 'Machado de Assis', 'Record', 'Romance', 1),
('O Cortiço', 'Aluísio Azevedo', 'Saraiva', 'Realismo', 2),
('Capitães da Areia', 'Jorge Amado', 'Companhia das Letras', 'Romance', 2);

-- Inserir empréstimos
INSERT INTO emprestimo (id_leitor, id_livro, data_emprestimo, data_devolucao, data_dev_realizad)
VALUES
(1, 1, '2025-10-15', '2025-10-25', '2025-10-15');


INSERT INTO emprestimo (id_leitor, id_livro, data_emprestimo, data_devolucao, data_dev_realizad)
VALUES
(1, 3, '2025-10-15', '2025-10-25', '2025-10-15');



