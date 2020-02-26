var carousel = new Vue({
    delimiters: ['[[', ']]'],
    el: '#carousel',
    data: {
    images : [
        "/static/media/dcu_campus/" + campus_data.id + "/1.png",
        "/static/media/dcu_campus/" + campus_data.id + "/2.png",
        "/static/media/dcu_campus/" + campus_data.id + "/3.png",
        "/static/media/dcu_campus/" + campus_data.id + "/4.png"
    ],
    timer: null,
    currentIndex: 0,
    campus_data: campus_data
},
mounted () {
    this.startCarousel();
},
methods: {
    startCarousel() {
        // console.log("here");
        this.timer = setInterval(this.nextImage, 3000);
    },
    nextImage() {
        this.currentIndex += 1;
        if (this.currentIndex > (this.images.length -1))
            this.currentIndex = 0;
        console.log(this.currentIndex);
    },
    prevImage() {
        this.currentIndex -= 1;
        if (this.currentIndex < 0)
            this.currentIndex = this.images.length - 1;
        console.log(this.currentIndex);
    }
},
computed: {
    currentImg() {
        return this.images[this.currentIndex];
    }
}
});

var restaurants = new Vue({
    el: '',
    data: {

    },
    mounted: {

    },
    filters: {
    },
    methods: {
        Capitalize: function(value) {
            if (!value) return ''
            value = value.toString()
            return value.charAt(0).toUpperCase() + value.slice(1)
        }
    },
    computed: {

    }
});