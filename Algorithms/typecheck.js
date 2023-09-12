function typeCheck(object) {
    // Use console.log() for debugging
    function validationType(key, value) {
        const parts = key.split('_')
        const typeHint = parts[parts.length - 1]
        console.log(typeHint)
        switch (typeHint) {
            case 'int':
                if (typeof value !== 'number' || !Number.isInteger(value)) {
                    throw new Error();
                }
                break;

            case 'string':
                if (typeof value !== 'string') {
                    throw new Error();
                }
                break;
            case 'bool':
                if (typeof value !== 'boolean') {
                    throw new Error();
                }
                break;
            default:
                throw new Error(`Unknown type hint ${typeHint} for property ${key}`);

        }
    }

    for (let key in object) {
        let value = object[key];
        Object.defineProperty(object, key, {
            get() {
                return value
            },
            set (newValue) {
                validationType(key, newValue);
                value = newValue
            }
        })
    }
}

const person = {
    name_string: "John",
    age_int: 30,
    isEmployed_bool: true
}

const obj = {
    age_int: 2,
    name_string: "Adam",
    job: null,
}
const validatingObject = typeCheck(obj)
validatingObject.age_int = "2"
