const a = document.getElementById("three");

const b = document.getElementById("four");

const c = document.getElementById("five");

a.addEventListener("submit", async(event) => {
    event.preventDefault();

    const aa = {
        name: a.three_one_name.value,
        password: a.three_two_name.value
    };

    try{
        const a_1 = await fetch("http://127.0.0.1:8000/users", { // функция fetch отправляет асинхронные http-запросы, возвращая объект response
            method: "POST",
            headers: {"Content-Type": "application/json"}, // Указывает что тело запроса будет в формате json
            body: JSON.stringify(aa) // Преобразование объекта в JSON и отправка в теле http-запроса
        });

        const a_2 = await a_1.json(); // преобразует response в формате json в объект js. await ожидает завершения асинхронного запроса
        console.log(a_2);

        console.log(a_2.name);
        console.log(a_2.password);
    }
    catch(err){
        console.error(err);
    }
});


b.addEventListener("submit", async(event) => {
    event.preventDefault();

    const name = b.four_one_name.value;

    try{
        const b_1 = await fetch(`http://127.0.0.1:8000/users/${name}`, {
            method: "GET",
            headers: {"Content-Type": "application/json"},
        });

        if (b_1.status === 404){
            console.error("User not found");
            return;
        }

        const b_2 = await b_1.json();
        console.log(b_2);
    }
    catch(err){
        console.error(err);
    }
});


c.addEventListener("click", async(event) => {
    event.preventDefault();

    try{
        const c_1 = await fetch("http://127.0.0.1:8000/users", {
            method: "GET",
            headers: {"Content-Type": "application/json"},
        });

        const c_2 = await c_1.json();
        console.log(c_2);
    }
    catch(err){
        console.error(err);
    }
});

//