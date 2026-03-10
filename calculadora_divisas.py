def exchange_money(budget, exchange_rate):
    return round(budget / exchange_rate, 2)


# tasas de hoy 9 de marzo 2026
# fuente: Banco Central RD y BBVA Mexico

dop_compra = 0.01671
dop_venta  = 0.01649

mxn_compra = 0.05908
mxn_venta  = 0.05540


budget = float(input("Cuanto dinero quieres convertir: "))

print("\nElige la conversion:")
print("1. USD a DOP")
print("2. DOP a USD")
print("3. USD a MXN")
print("4. MXN a USD")
print("5. DOP a MXN")
print("6. MXN a DOP")

opcion = input("\nEscribe el numero: ")

if opcion == "1":
    print("Resultado (compra):", exchange_money(budget, dop_compra))
    print("Resultado (venta):", exchange_money(budget, dop_venta))

elif opcion == "2":
    print("Resultado (compra):", exchange_money(budget, 1 / dop_compra))
    print("Resultado (venta):", exchange_money(budget, 1 / dop_venta))

elif opcion == "3":
    print("Resultado (compra):", exchange_money(budget, mxn_compra))
    print("Resultado (venta):", exchange_money(budget, mxn_venta))

elif opcion == "4":
    print("Resultado (compra):", exchange_money(budget, 1 / mxn_compra))
    print("Resultado (venta):", exchange_money(budget, 1 / mxn_venta))

elif opcion == "5":
    dop_a_mxn = dop_compra / mxn_venta
    print("Resultado:", exchange_money(budget, dop_a_mxn))

elif opcion == "6":
    mxn_a_dop = mxn_compra / dop_venta
    print("Resultado:", exchange_money(budget, mxn_a_dop))