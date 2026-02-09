<script lang="ts">

import type { PageData } from "./$types";

const { data } = $props<{message: PageData}>();

</script>



<div class="flex items-center justify-center">
    <h2>{data.message}</h2>
</div>

