@client.command()
async def car(ctx):
    cars = ('Acura', 'Alfa Romeo', 'Aston Martin', 'Audi', 'Bentley', 'BMW', 'Bugatti', 'Buick', 'Cadillac', 'Chevrolet', 'Chryler', 'Citroen', 'Dodge', 'Ferrari', 'Fiat', 'Ford', 'Geely', 'General Motors', 'GMC', 'Honda', 'Hyundai', 'Infinti', 'Jaguar', 'Jeep', 'Kia Motors', 'Koenigsegg', 'Lamborghini', 'Land Rover', 'Lexus', 'Maserati', 'Mazda', 'McLaren', 'Mercedez-Benz', 'Mini', 'Mitsubishi', 'Nissan', 'Pagani', 'Peugeot', 'Porsche', 'RAM', 'Renault', 'Rolls-Royce', 'SAAB', 'Subaru', 'Suzuki', 'Tata Motors', 'Tesla', 'Toyota', 'Volkswagen', 'Volvo')
        message = await ctx.send("""```
    _______
    /|_||_\`.__
    (   _    _ _|
    =`-(_)--(_)-' 
        ```""")
        await message.edit(content="""```
        _______
        /|_||_\`.__
        (   _    _ _|
        =`-(_)--(_)-' 
        ```""")
        await message.edit(content="""```
            _______
            /|_||_\`.__
            (   _    _ _|
            =`-(_)--(_)-' 
        ```""")
        await message.edit(content="""```
                _______
                /|_||_\`.__
                (   _    _ _|
                =`-(_)--(_)-' 
        ```""")
        await message.edit(content="""```
                        _______
                        /|_||_\`.__
                        (   _    _ _|
                        =`-(_)--(_)-' 
        ```""")
        await message.edit(content="""```
                                _______
                                /|_||_\`.__
                                (   _    _ |
                                =`-(_)--(_)-' 
        ```""")
        k = f'Answer: {random.choice(cars)}'
        await message.edit(content=f"""```
                                _______
                                /|_||_\`.__
                            {k} (   _    _ |
                                =`-(_)--(_)-' 
        ```""")
