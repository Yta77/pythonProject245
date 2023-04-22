import plotly.figure_factory as ff

df = [dict(Task="Ener2crowd Finalizzare Accordo (Pricing) ", Start='2023-04-24', Finish='2023-04-27', Resource='Not Started'),
      dict(Task="Rivedere Pricing ", Start='2023-04-26', Finish='2023-05-06', Resource='Incomplete'),
      dict(Task="Preparare Brochure Commerciale Italiano ", Start='2023-04-17', Finish='2023-04-21', Resource='Complete'),
      dict(Task="Go 2 Market Strategy ", Start='2023-04-24', Finish='2023-05-18', Resource='Incomplete'),
      dict(Task="Review Funnel Commerciale e Aggiornamento Database lead ", Start='2023-04-17', Finish='2023-04-19', Resource='Complete'),
      dict(Task="Meeting Commerciali", Start='2023-04-24', Finish='2023-04-28', Resource='Not Started'),
      dict(Task="Meeting IKB Societa Oil Tedesca", Start='2023-04-26', Finish='2023-04-26', Resource='Not Started'),
      dict(Task="Lavorare su Bando ISI INAIL con Gabriele", Start='2023-04-26', Finish='2023-05-05', Resource='Incomplete'),
      dict(Task="Simulatore Valore della CER", Start='2023-04-18', Finish='2023-05-03', Resource='Incomplete')]

colors = {'Not Started': 'rgb(220, 0, 0)',
          'Incomplete': (1, 0.9, 0.16),
          'Complete': 'rgb(0, 255, 100)'}

fig = ff.create_gantt(df, colors=colors, index_col='Resource', show_colorbar=True,
                      group_tasks=True)
fig.show()