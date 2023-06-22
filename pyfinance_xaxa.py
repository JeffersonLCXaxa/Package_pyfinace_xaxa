import matplotlib.pyplot as plt

class PyFinance:
    @staticmethod
    def simple_interest(period, rate, initial_capital):
        rate = rate / 100
        interest = initial_capital * rate * period
        total = initial_capital + interest
        return total

    @staticmethod
    def percentage(percentage, value, discount=False, add=False):
        if discount and not add:
            return value - ((abs(percentage) / 100) * value)
        elif not discount and add:
            return value + ((abs(percentage) / 100) * value)
        elif discount and add:
            return "Error: discount and addition cannot both be 'True' in the same calculation."
        else:
            return (percentage / 100) * value

    @staticmethod
    def future_value(period, rate, initial_capital, monthly=0, graphic=False):
        rate = rate / 100
        future_values = []

        for periodo in range(period):
            montante_periodo = initial_capital * (1 + rate) ** (periodo + 1) + monthly * (((1 + rate) ** (periodo + 1) - 1) / rate)
            future_values.append(montante_periodo)

        if not graphic:
            resultado = [round(valor, 2) for valor in future_values]
            print(f'0: {round(initial_capital, 2)}')

            for indice, valor in enumerate(resultado, start=1):
                print(f'{indice}: {valor}')

            investimento = initial_capital + (period * monthly)
            juros_obtidos = future_values[-1] - investimento

            print(f"\nInvestment: {round(investimento, 2)}")
            print(f"Income: {round(juros_obtidos, 2)}")

        elif graphic:
            if period >= 12:
                num_plots = period // 12
                remainder = period % 12
                if remainder > 0:
                    num_plots += 1

                fig, axs = plt.subplots(num_plots, figsize=(10, num_plots * 6))
                plt.subplots_adjust(hspace=0.5)

                for i in range(num_plots):
                    start = i * 12
                    end = start + 12 if i < num_plots - 1 else period
                    values = future_values[start:end]
                    periods = range(start + 1, end + 1)

                    if num_plots > 1:
                        ax = axs[i]
                    else:
                        ax = axs

                    ax.barh(periods, values)
                    ax.set_xlabel('Future Values')
                    ax.set_ylabel('Periods')
                    ax.set_title(f'Future Values for Periods {start + 1} to {end}')

                    for value, periodo in zip(values, periods):
                        ax.text(value, periodo, f'{value:.2f}', ha='right', va='center')

                    ax.set_xlim(initial_capital, max(future_values))

                    ax.get_xaxis().set_visible(False)

                plt.show()
        else:
            print("Erro: invalid graphic parameter. Assign True or False.")