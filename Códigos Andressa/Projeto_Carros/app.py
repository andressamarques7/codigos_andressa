import streamlit as st 
#### COLOCA UM TITULO E UM SLOGAN NA BARRA LATERAL
st.sidebar.title("ALUGUEL DE CARROS")
st.sidebar.write("Mais que um carro, sua liberdade sobre rodas!")

### COLOCA UMA IMAGEM(NESSE CASO UMA LOGO)
st.sidebar.image("logo.png")

### ESCREVE PARA SELECIONAR O CARRO 
st.sidebar.write("Escolha o carro ideal para você!!")

### LISTA DE CARROS
carros = ["Porsche 911 Turbo S", "BMW Série 1", "Ford Mustang Shelby GT500", "Ford Ka", "Honda Civic", "Hyundai Onix"]

### OPÇÃO PARA SELECIONAR O CARRO
opcao = st.sidebar.selectbox("Escolha uma carro:", carros)

### TÍTULO PARA MOSTRAR O CARRO QUE ALUGOU
st.markdown(f"## AURA")
st.markdown("---")
st.markdown(f"## Você alugou o modelo: {opcao}")
st.write(f"Ótima escolha! Esse carro é mais do que um carro!!")

### COMANDO PARA MOSTRAR A FOTO NA OPÇÃO DE CARRO ESCOLHIDA
st.image(f"{opcao}.png")
st.markdown("---")


dias = st.text_input(f"Por quantos dias o {opcao} foi alugado?")
km = st.text_input(f"Quantos km você rodou com o {opcao}?")

if opcao == "Porsche 911 Turbo S":
    diaria = 750

elif opcao == "BMW Série 1":
    diaria = 700

elif opcao ==  "Ford Mustang Shelby GT500":
    diaria = 850 

elif opcao == "Ford Ka":
    diaria = 300

elif opcao == "Honda Civic":
    diaria = 420

elif opcao == "Hyundai Onix":
    diaria = 350


if st.button("Calcular"):
    dias = int(dias)
    km = float(km)

    total_dias = dias * diaria
    total_km = km * 0.15
    aluguel_total = total_dias + total_km

    st.warning(f'Você alugou o {opcao} por {dias} dias e rodou {km}km. O valor total a pagar é R$ {aluguel_total:.2f}. Que a sua experiência tenha sido ótima e surreal, agradecemos a preferência por ter escolhido a Aura!')








