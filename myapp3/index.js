import fetch from "node-fetch"

const URL = 'http://127.0.0.1:8000/student/'
const URL2 = 'http://127.0.0.1:8000/student/1'

const get_data = async() => {
    try {
        const response = await fetch(URL)
        const jsonData = await response.json()
        console.log(jsonData)
    } catch (error) {
        console.error(error)
    }
}

get_data()