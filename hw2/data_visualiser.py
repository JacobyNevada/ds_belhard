import pandas as pd

import seaborn as sns
import matplotlib.pyplot as plt

class Data_Visualiser:
  def visualise_pairplot(dataset, category):
    sample_data = dataset.head(50)
    # Построение парных графиков при помощи sns
    sns.pairplot(sample_data, hue=category)
    plt.show()


  def visualise_histogram(dataset):
    # Установка стиля Seaborn для красивых графиков
    sns.set(style="whitegrid")

    # Создание гистограмм для каждой числовой переменной
    dataset.hist(bins=20, figsize=(15, 10), color='skyblue', edgecolor='black')

    # Добавление названий для каждого графика и осей
    for ax in plt.gcf().get_axes():
      ax.set_xlabel('Значение')
      ax.set_ylabel('Частота')
      #ax.set_title(ax.get_title().replace('wine_class', 'Класс вина'))

    # Регулировка макета для предотвращения наложения подписей
    plt.tight_layout()

    # Показать график
    plt.show()


  def visualise_heatmap(dataset):
    sns.set(style="white")

    # Расчет корреляционной матрицы только для числовых данных
    numeric_df = dataset.select_dtypes(include=[np.number])  # Исключаем нечисловые столбцы
    corr = numeric_df.corr()

    # Маска для отображения только нижней треугольной части матрицы (опционально)
    mask = np.triu(np.ones_like(corr, dtype=bool))

    # Настройка цветовой палитры
    cmap = sns.diverging_palette(230, 20, as_cmap=True)

    # Создание тепловой карты
    plt.figure(figsize=(12, 10))
    sns.heatmap(corr, mask=mask, cmap=cmap, vmax=.3, center=0,
                square=True, linewidths=.5, cbar_kws={"shrink": .5}, annot=True)

    # Добавление заголовка
    plt.title('Тепловая карта корреляций', fontsize=20)

    # Показать график
    plt.show()

  def visualise_boxplot(dataset):
    sns.set(style="whitegrid")

    # Создаем ящики с усами для каждой колонки в DataFrame
    plt.figure(figsize=(12, 10))

    # Перебираем каждый числовой столбец и создаем для него ящик с усами
    for index, column in enumerate(dataset.select_dtypes(include=[np.number]).columns):
      plt.subplot((len(dataset.columns) // 3) + 1, 3, index + 1)
      sns.boxplot(y=dataset[column])

    plt.tight_layout()
    plt.show()

  def visualise_lineplot(dataset, numeric_features):
    sns.set(style="whitegrid")

    # Создаем сетку графиков
    fig, axes = plt.subplots(len(numeric_features), 1, figsize=(15, 20))

    # Для случая с одним графиком (если нужен только один столбец)
    if len(numeric_features) == 1:
        axes = [axes]

    datahead = dataset.head(20)

    # Строим line plot для каждого числового столбца
    for i, column in enumerate(numeric_features):
        axes[i].plot(datahead.index, datahead[column], marker='o', linestyle='-',
                    linewidth=2, markersize=3, alpha=0.7)
        axes[i].set_xlabel('Индекс наблюдения')
        axes[i].set_ylabel('Значение')
        axes[i].set_title(f'Линейный график: {column}')
        axes[i].grid(True, alpha=0.3)

    # Регулировка макета для предотвращения наложения подписей
    plt.tight_layout()

    # Показать график
    plt.show()


  def visualise_all_types(dataset, numeric_features, category):
    visualise_pairplot(dataset, category)
    visualise_histogram(dataset)
    visualise_heatmap(dataset)
    visualise_boxplot(dataset)
    visualise_lineplot(dataset, numeric_features)
