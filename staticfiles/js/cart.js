// Find out the cart items from localStorage
if (localStorage.getItem('cart') == null) {
    var cart = {};
} else {
    cart = JSON.parse(localStorage.getItem('cart'));
    updateCart(cart);

}
// If the add to cart button is clicked, add/increment the item
//$('.cart').click(function() {
$('.divpr').on('click', 'button.cart', function () {
    var idstr = this.id.toString();
    if (cart[idstr] != undefined) {
        qty = cart[idstr][0] + 1;
    } else {
        qty = 1;
        nam = document.getElementById('name' + idstr).innerHTML;
        price = document.getElementById('price' + idstr).innerHTML;
        console.log(prc)
        cart[idstr] = [qty, nam, price];



    }
    updateCart(cart);

});
//Add Popover to cart
$('#popcart').popover();
updatepopover(cart)


function updatepopover() {
    console.log('we are inside');
    var popStr ="";
    popStr = popStr + "<h5>cart for your item in my cart</h5>";
    var i = 1;
    for (var item in cart){
        popStr = popStr + "<b>" + i + "</b>. ";
        popStr = popStr + document.getElementById('name' + item).innerHTML +  "Qty: " + cart[item][0] + "Prc: " + cart[item][2];
        i = i + 1;

    }
    popStr = popStr + "</div> <a href = '/Shop/checkout'><button class='btn btn-secondary cart' id='Checkout'>Checkout</button></a> <button class='btn btn-secondary cart' onclick='clearcart()' id='clearcart'>Clearcart</button>"
    console.log(popStr)
    document.getElementById('popcart').setAttribute('data-content', popStr);
    $('#popcart').popover('show');




}
// clear cart

function clearcart() {
    cart =JSON.parse(localStorage.getItem('cart'));
    for (var item in cart){

        document.getElementById('div' + item).innerHTML = '<button id="' + item + '" class="btn btn-secondary cart">Buy</button>'
    }
    localStorage.clear();
    cart = {}
    updateCart(cart);

}

function updateCart(cart) {
    var sum = 0;
    for (var item in cart) {
        sum = sum + cart[item][0];
        document.getElementById('div' + item).innerHTML = "<button id='minus" + item + "' class='btn btn-primary minus'>-</button> <span id='val" + item + "''>" + cart[item][0] + "</span> <button id='plus" + item + "' class='btn btn-primary plus'> + </button>";
    }
    localStorage.setItem('cart', JSON.stringify(cart));
    document.getElementById('cart').innerHTML = sum;
    console.log(cart);
    updatepopover(cart)
}
// If plus or minus button is clicked, change the cart as well as the display value
$('.divpr').on("click", "button.minus", function() {
    a = this.id.slice(7, );
    cart['pr' + a][0] = cart['pr' + a][0] - 1;
    cart['pr' + a][0] = Math.max(0, cart['pr' + a][0]);
    document.getElementById('valpr' + a).innerHTML = cart['pr' + a][0];
    updateCart(cart);
});
$('.divpr').on("click", "button.plus", function() {
    a = this.id.slice(6, );
    cart['pr' + a][0] = cart['pr' + a][0] + 1;
    document.getElementById('valpr' + a).innerHTML = cart['pr' + a][0];
    updateCart(cart);
});

