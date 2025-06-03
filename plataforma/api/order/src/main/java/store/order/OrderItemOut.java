package store.order;

import java.io.Serializable;

import lombok.Builder;
import lombok.experimental.Accessors;
import store.product.ProductOut;

@Builder 
@Accessors(fluent = true)
public record OrderItemOut(
    String id,
    ProductOut product,
    Integer quantity,
    Double total
) implements Serializable {
}